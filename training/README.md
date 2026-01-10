# 🍅 Tomato Leaf Disease Detection – Model Training & Evaluation



This folder contains the training and evaluation notebooks used to develop the deep learning models
for the Tomato Leaf Disease Detection system.

The focus here is on dataset preparation, model training, and performance evaluation.
Production deployment and inference architecture are documented in the main repository README.

---

## 📂 Dataset Overview

The dataset consists of tomato leaf images belonging to 10 disease categories.

### Dataset Split

| Split       | Images | Classes |
|------------|--------|---------|
| Training   | 18,339 | 10      |
| Validation | 2,289  | 10      |
| Test       | 2,302  | 10      |

### Classes
- Tomato___Bacterial_spot
- Tomato___Early_blight
- Tomato___Late_blight
- Tomato___Leaf_Mold
- Tomato___Septoria_leaf_spot
- Tomato___Spider_mites (Two-spotted spider mite)
- Tomato___Target_Spot
- Tomato___Tomato_Yellow_Leaf_Curl_Virus
- Tomato___Tomato_mosaic_virus
- Tomato___healthy

---

## 🏗️ Model Architecture

Both models were used as feature extractors with a custom fully connected classification head.

### Common Strategy
- Pretrained CNN backbone (ImageNet)
- Frozen convolutional layers
- Custom classifier head:
  - Global Average Pooling
  - Dense (ReLU)
  - Batch Normalization
  - Dropout
  - Softmax output layer (10 classes)

---

## 📊 Model Performance (Test Dataset)

### 🔹 ResNet50 (Feature Extractor)

**Overall Test Accuracy:** 96%

| Class | Precision | Recall | F1-score |
|------|----------|--------|----------|
| Bacterial Spot | 0.99 | 0.98 | 0.98 |
| Early Blight | 0.97 | 0.93 | 0.95 |
| Late Blight | 0.98 | 0.98 | 0.98 |
| Leaf Mold | 1.00 | 0.90 | 0.95 |
| Septoria Leaf Spot | 0.96 | 0.98 | 0.97 |
| Spider Mites | 0.89 | 0.99 | 0.94 |
| Target Spot | 0.90 | 0.92 | 0.91 |
| Yellow Leaf Curl Virus | 1.00 | 0.98 | 0.99 |
| Mosaic Virus | 1.00 | 0.99 | 1.00 |
| Healthy | 0.96 | 1.00 | 0.98 |

**Macro Avg F1-score:** 0.96  
**Weighted Avg F1-score:** 0.96  

---

### 🔹 EfficientNetB0 (Feature Extractor)

**Overall Test Accuracy:** 96%

| Class | Precision | Recall | F1-score |
|------|----------|--------|----------|
| Bacterial Spot | 0.99 | 0.99 | 0.99 |
| Early Blight | 1.00 | 0.91 | 0.95 |
| Late Blight | 0.95 | 0.99 | 0.97 |
| Leaf Mold | 0.98 | 0.96 | 0.97 |
| Septoria Leaf Spot | 0.96 | 0.93 | 0.95 |
| Spider Mites | 0.93 | 0.95 | 0.94 |
| Target Spot | 0.83 | 0.97 | 0.89 |
| Yellow Leaf Curl Virus | 1.00 | 0.97 | 0.98 |
| Mosaic Virus | 1.00 | 0.98 | 0.99 |
| Healthy | 0.98 | 0.95 | 0.96 |

**Macro Avg F1-score:** 0.96  
**Weighted Avg F1-score:** 0.96  

---

## 📌 Key Observations

- Both models achieved strong generalization with 96% test accuracy.
- ResNet50 showed more stable performance across visually similar disease classes.
- EfficientNetB0 achieved comparable accuracy with fewer parameters.
- Both models are suitable for production inference and A/B testing.


