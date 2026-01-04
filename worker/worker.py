import json
import time
import numpy as np
from PIL import Image
from io import BytesIO

from app.redis_conn import redis_client
from app.preprocess import preprocess_image
from app.model import load_model

models = {
    "v1": load_model("v1"),
    "v2": load_model("v2")
}
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
print("Worker started...")

while True:
    tasks = redis_client.hgetall("tasks")

    for task_id, data in tasks.items():
        payload = json.loads(data)
        image_bytes = bytes.fromhex(payload["image"])
        version = payload["version"]

        image = Image.open(BytesIO(image_bytes))
        processed = preprocess_image(image)

        preds = models[version].predict(processed)
        idx = int(np.argmax(preds))
        confidence = float(np.max(preds))
        disease = CLASS_LABELS[idx]

        redis_client.hset(
            "results",
            task_id,
            json.dumps({
                "disease": disease,
                "confidence": round(confidence * 100, 2)
                
            })
        )

        redis_client.hdel("tasks", task_id)

    time.sleep(1)
