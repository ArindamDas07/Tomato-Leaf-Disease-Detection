# 🍅 Tomato Leaf Disease Detection – Model Training

This directory contains the **model training pipelines** for two CNN-based image classification models used in a **production-grade ML inference system with A/B testing**.

Both models are trained on the **same dataset**, using the **same preprocessing and training strategy**.  
The **only difference** between the two versions is the **number of convolutional filters**, enabling a **fair and controlled architectural comparison**.

---

## 📂 Directory Structure

```
training/
│
├── Tomato_Leaf_Disease_Training_v1.ipynb
├── Tomato_Leaf_Disease_Training_v2.ipynb
└── README.md
```

---

## 📊 Dataset Information

**Dataset Name:** Tomato Leaf Disease Dataset  
**Source:** Kaggle  
**Link:** https://www.kaggle.com/datasets/shylesh101/tomato-leaf-disease  

### Dataset Summary

| Property | Value |
|--------|------|
| Total Images | 22,980 |
| Number of Classes | 10 |
| Image Type | RGB |
| Structure | Folder-based (class-wise) |

---

## 🧠 Model Versions Overview

| Model Version | Key Difference | Test Accuracy |
|--------------|----------------|---------------|
| **v1** | Reduced CNN filters | **96%** |
| **v2** | Increased CNN filters | **94%** |

All other architectural components and training strategies are **identical**.

---

## 🏗️ Common Model Architecture

```
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
```

---

## 🔑 Key Training Techniques

### Batch Normalization
- Improves convergence
- Stabilizes gradients
- Reduces covariate shift

### Dropout (0.33)
- Prevents overfitting
- Improves generalization

### Early Stopping
```python
EarlyStopping(
    monitor="val_loss",
    min_delta=0.0001,
    patience=3
)
```

---

## ⚙️ Training Configuration

```python
optimizer = 'adam'
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
metrics = ['accuracy']
```

---

## 🖼️ Data Augmentation

```python
ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,
    horizontal_flip=True
)
```

---

## 🧪 Evaluation Results

| Model | Accuracy |
|------|----------|
| v1 | 96% |
| v2 | 94% |

---

## 🚀 Why This Matters

- Demonstrates controlled experimentation
- Production-ready mindset
- Clean separation of training & inference
- Suitable for A/B testing in real systems

---

## 🔗 Related Project

These models are deployed in a **Dockerized, scalable ML inference system** using:
- FastAPI
- Redis
- Background workers
- NGINX
- Model version routing

Refer to the main repository README for deployment details.
