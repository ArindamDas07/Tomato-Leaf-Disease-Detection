🍅 Tomato Leaf Disease Detection – Model Training

This directory contains the training pipelines for two CNN-based models used in a production-ready ML inference system with A/B testing.

Both models are trained on the same dataset, using the same preprocessing and training strategy.
The only difference between the two versions is the number of convolution filters, allowing a fair architectural comparison.

📂 Training Files
training/
│
├── Tomato_Leaf_Disease_Training_v1.ipynb
├── Tomato_Leaf_Disease_Training_v2.ipynb
└── README.md

📊 Dataset

Name: Tomato Leaf Disease Dataset

Source: Kaggle

Link:
👉 https://www.kaggle.com/datasets/shylesh101/tomato-leaf-disease 

Dataset Summary

Total images: 22,980

Number of classes: 10

Type: RGB leaf images

Structure: Folder-based (class-wise)

🧠 Model Versions Overview
Model Version	Difference	Test Accuracy
v1	Reduced number of CNN filters	96%
v2	Higher number of CNN filters	94%

✅ All other architectural components and training strategies are identical.

This setup enables controlled A/B testing in production.

🏗️ Model Architecture (Common for v1 & v2)
Input Image
↓
Batch Normalization
↓
Conv2D + ReLU
↓
MaxPooling
↓
Batch Normalization
↓
Conv2D + ReLU
↓
MaxPooling
↓
Batch Normalization
↓
Conv2D + ReLU
↓
MaxPooling
↓
Flatten
↓
Dense (ReLU)
↓
Dropout
↓
Dense (Softmax)

🔑 Key Training Techniques Highlighted
✅ Batch Normalization

Stabilizes training

Improves convergence speed

Reduces internal covariate shift

✅ Dropout (0.33)

Prevents overfitting

Encourages model generalization

✅ Early Stopping
EarlyStopping(
    monitor="val_loss",
    min_delta=0.0001,
    patience=3
)


Stops training automatically when validation loss stops improving

Prevents unnecessary epochs and overfitting

⚙️ Training Configuration
optimizer = 'adam'
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
metrics = ['accuracy']


Optimizer: Adam (adaptive learning rate)

Loss Function: Sparse Categorical Crossentropy

Metric: Accuracy

🖼️ Data Augmentation
ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,
    horizontal_flip=True
)


Applied to improve robustness against:

Rotation variance

Orientation changes

Lighting differences

🧪 Evaluation Result (Example – v1)
Loss: 0.1705
Accuracy: 96%


Both models were evaluated on a held-out test set.

🚀 Why This Training Setup Matters

Demonstrates controlled experimentation

Suitable for production A/B testing

Clean separation between training and inference

Follows industry ML best practices

Easily extendable for future versions (v3, v4…)

🔗 Related Project

These trained models are deployed in a Dockerized ML inference system with:

FastAPI

Redis queue

Background workers

NGINX reverse proxy

Version-based model routing (A/B testing)

👉 See main repository README for deployment details.