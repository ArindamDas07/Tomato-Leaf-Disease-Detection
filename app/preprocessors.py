import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as eff_preprocess
from io import BytesIO

def preprocess(image_bytes, model_type):
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    arr = np.array(image)

    if model_type == "resnet":
        arr = resnet_preprocess(arr)
    elif model_type == "efficientnet":
        arr = eff_preprocess(arr)
    else:
        raise ValueError("Unknown model type")

    return np.expand_dims(arr, axis=0)
