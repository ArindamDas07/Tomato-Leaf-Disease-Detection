import uuid
import json
from app.redis_conn import redis_client

def enqueue_task(image_bytes, model_version):
    task_id = str(uuid.uuid4())

    redis_client.hset(
        "tasks",
        task_id,
        json.dumps({
            "image": image_bytes.hex(),
            "version": model_version
        })
    )
    return task_id
