import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
import logging

logger = logging.getLogger(__name__)
_MODELS = {}

def load_resnet():
    if "resnet" not in _MODELS:
        _MODELS["resnet"] = tf.keras.models.load_model(
            "models/resnet/tomato_resnet_model.h5",
            compile=False
        )
        logger.info("✅ ResNet50 loaded")
    return _MODELS["resnet"]

def load_efficientnet():
    if "efficientnet" not in _MODELS:
        base = EfficientNetB0(
            weights=None,
            include_top=False,
            input_shape=(224, 224, 3)
        )
        base.trainable = False

        x = base.output
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(256, activation="relu")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.5)(x)
        output = layers.Dense(10, activation="softmax")(x)

        model = models.Model(inputs=base.input, outputs=output)
        model.load_weights("models/efficientnet/efficientnetb0_tomato_96pct_weights.h5")

        _MODELS["efficientnet"] = model
        logger.info("✅ EfficientNetB0 loaded")

    return _MODELS["efficientnet"]
