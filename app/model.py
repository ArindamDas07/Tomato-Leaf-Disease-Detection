import tensorflow as tf
import os
import logging

logger = logging.getLogger(__name__)

BASE_PATH = "models"

def load_model(version: str):
    """
    Loads a TensorFlow model based on version.
    
    version: "v1" or "v2"
    """
    if version == "v1":
        model_file = "Tomato_model_v1.h5"
    elif version == "v2":
        model_file = "Tomato_model_v2.h5"
    else:
        raise ValueError(f"Unknown model version: {version}")

    model_path = os.path.join(BASE_PATH, version, model_file)

    logger.info(f"Loading model from {model_path}")

    return tf.keras.models.load_model(
        model_path,
        compile=False   # ✅ REQUIRED for inference-only production systems
    )
