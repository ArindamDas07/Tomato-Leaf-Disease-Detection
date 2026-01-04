from PIL import Image
import numpy as np

def preprocess_image(image):
    image = image.resize((32, 32))
    arr = np.array(image) / 255.0
    return np.expand_dims(arr, axis=0)
