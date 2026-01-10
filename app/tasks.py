import numpy as np
import time
import logging
import socket

from app.celery_app import celery_app
from app.model_registry import load_resnet, load_efficientnet
from app.preprocessors import preprocess

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("inference")

# ---------------- CLASS LABELS ----------------
CLASS_LABELS = [
    "Bacterial_spot",
    "Early_blight",
    "Late_blight",
    "Leaf_Mold",
    "Septoria_leaf_spot",
    "Spider_mites",
    "Target_Spot",
    "Yellow_Leaf_Curl_Virus",
    "Mosaic_virus",
    "Healthy"
]

# ---------------- CELERY TASK ----------------
@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=5,
    retry_kwargs={"max_retries": 3}
)
def run_inference(self, image_bytes, model_type):
    start_time = time.time()
    worker_name = socket.gethostname()

    logger.info(
        f"🚀 Inference started | model={model_type} | worker={worker_name}"
    )

    # Load model
    if model_type == "resnet":
        model = load_resnet()
    else:
        model = load_efficientnet()

    # Preprocess & predict
    processed = preprocess(image_bytes, model_type)
    preds = model.predict(processed)

    idx = int(np.argmax(preds))
    confidence = float(np.max(preds))
    latency = round(time.time() - start_time, 3)

    logger.info(
        f"✅ Prediction completed | "
        f"model={model_type} | "
        f"class={CLASS_LABELS[idx]} | "
        f"confidence={confidence:.4f} | "
        f"latency={latency}s | "
        f"worker={worker_name}"
    )

    return {
        "disease": CLASS_LABELS[idx],
        "confidence": round(confidence * 100, 2)
    }
