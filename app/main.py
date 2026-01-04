from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.tasks import enqueue_task
from app.redis_conn import redis_client

import time
import json
import logging


# =========================================================
# APP INITIALIZATION
# =========================================================
app = FastAPI(title="Tomato Leaf Disease Detection System")

# Templates (Frontend)
templates = Jinja2Templates(directory="templates")

# Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# =========================================================
# LOGGING (PRODUCTION OBSERVABILITY)
# =========================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


# =========================================================
# HEALTH CHECK (LOAD BALANCER / K8s)
# =========================================================
@app.get("/health")
def health():
    """
    Used by:
    - NGINX
    - Kubernetes readiness/liveness probes
    """
    return {"status": "ok"}


# =========================================================
# FRONTEND ENTRY POINT
# =========================================================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Serves the frontend UI.
    Stateless → scalable.
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# =========================================================
# PREDICTION ENDPOINT
# =========================================================
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Async prediction endpoint.
    - Sends task to Redis
    - Worker does inference
    - API polls result (demo approach)
    """

    # -----------------------------------------------------
    # INPUT VALIDATION
    # -----------------------------------------------------
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed"
        )

    image_bytes = await file.read()

    # -----------------------------------------------------
    # A/B TESTING (50-50 TRAFFIC SPLIT)
    # -----------------------------------------------------
    """
    Same model file used for v1 and v2.
    In real systems, versions differ.
    """
    model_version = "v1" if int(time.time()) % 2 == 0 else "v2"

    logger.info(f"Dispatching task to model version: {model_version}")

    # -----------------------------------------------------
    # ENQUEUE TASK (ASYNC INFERENCE)
    # -----------------------------------------------------
    task_id = enqueue_task(image_bytes, model_version)

    # -----------------------------------------------------
    # RESULT POLLING (WITH TIMEOUT)
    # -----------------------------------------------------
    """
    Simple polling for demo.
    Production systems use:
    - WebSockets
    - Callbacks
    - Async queues
    """
    timeout_seconds = 10
    start_time = time.time()

    while True:
        result = redis_client.hget("results", task_id)

        if result:
            logger.info(f"Task {task_id} completed")
            return json.loads(result)

        if time.time() - start_time > timeout_seconds:
            logger.error(f"Task {task_id} timed out")
            raise HTTPException(
                status_code=504,
                detail="Inference timed out"
            )

        time.sleep(0.3)
