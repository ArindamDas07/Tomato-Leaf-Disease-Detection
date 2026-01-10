from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.tasks import run_inference
from celery.result import AsyncResult

import time

app = FastAPI(title="Tomato Leaf Disease Detection")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files allowed")

    image_bytes = await file.read()
    # A/B testing
    model_type = "resnet" if int(time.time()) % 2 == 0 else "efficientnet"

    # Send async task
    task = run_inference.delay(image_bytes, model_type)

    return {
        "task_id": task.id,
        "status": "queued",
        "model_assigned": model_type
    }


@app.get("/result/{task_id}")
def get_result(task_id: str):
    task = AsyncResult(task_id, app=run_inference.app)

    if task.state == "PENDING":
        return {"status": "pending"}

    if task.state == "SUCCESS":
        return task.result

    if task.state == "FAILURE":
        return {"status": "failed", "error": str(task.info)}

    return {"status": task.state}
