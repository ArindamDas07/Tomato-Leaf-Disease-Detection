# 🍅 Tomato Leaf Disease Detection  
## Production-Grade Deep Learning Inference System

A **production-ready deep learning system** for tomato leaf disease classification, featuring **asynchronous inference**, **horizontal scalability**, **multi-model support**, and a **Dockerized microservices architecture**.

This project goes beyond notebooks and demonstrates **how ML models are deployed, served, and scaled in real-world systems**.

---

## 🚀 Key Features

- ✅ Deep learning–based tomato leaf disease classification (**10 classes**)
- ✅ **Asynchronous inference** using **FastAPI + Celery + Redis**
- ✅ **Horizontally scalable** Celery worker pool
- ✅ **Multi-model support** (ResNet50 & EfficientNetB0)
- ✅ **Nginx reverse proxy** as production entry point
- ✅ **Stateless FastAPI backend**
- ✅ **Docker & Docker Compose**–based deployment
- ✅ Web UI for image upload and result visualization

---

## 📂 Dataset Overview

The models were trained on a tomato leaf disease dataset containing **10 classes**.

### Dataset Split

| Split       | Images | Classes |
|------------|--------|---------|
| Training   | 18,339 | 10 |
| Validation | 2,289  | 10 |
| Test       | 2,302  | 10 |

### Disease Classes

- Bacterial Spot  
- Early Blight  
- Late Blight  
- Leaf Mold  
- Septoria Leaf Spot  
- Spider Mites (Two-spotted spider mite)  
- Target Spot  
- Tomato Yellow Leaf Curl Virus  
- Tomato Mosaic Virus  
- Healthy  

---

## 🧠 Models Used

Both models are used as **feature extractors** with a **custom fully connected classification head**.

### 🔹 ResNet50
- Pretrained on ImageNet
- Backbone frozen
- Custom dense classifier head
- Strong and stable class-wise performance

### 🔹 EfficientNetB0
- Lightweight and compute-efficient
- Competitive accuracy
- Better suited for production and resource-constrained environments

📌 **A/B testing is implemented at inference time** to route requests between models.

---

## 📊 Model Performance (Test Set)

| Model           | Accuracy | Macro F1 | Weighted F1 |
|----------------|----------|----------|-------------|
| ResNet50       | 96%      | 0.96     | 0.96        |
| EfficientNetB0 | 96%      | 0.96     | 0.96        |

📎 Detailed per-class metrics, confusion matrices, and training notebooks are available in the **`training/`** folder.

---

## ⚙️ Production Architecture

### 🔄 End-to-End Inference Flow
---
```text
User (Browser / Client)
        |
        | Upload Image
        v
FastAPI API (POST /predict)
        |
        | Async task queued
        v
Redis (Task Queue)
        |
        | Task picked by worker
        v
Celery Worker
  ├─ Load Model (ResNet / EfficientNet)
  ├─ Preprocess Image
  └─ Predict Disease
        |
        | Store result
        v
Redis (Result Backend)
        |
        | Poll via GET /result/{task_id}
        v
FastAPI API
        |
        v
Frontend UI (Browser)
  ├─ Display Disease
  └─ Display Confidence


---

### 📌 Architecture Notes

- The **frontend never communicates directly with Redis**
- Redis is accessed **only by FastAPI and Celery**
- FastAPI acts as the **secure API gateway**
- Polling via `GET /result/{task_id}` enables **non-blocking UX**
- Designed for **horizontal scalability**

---

## 🌐 Web Interface

- Built using **HTML, CSS, and vanilla JavaScript**
- Image preview before upload
- Asynchronous polling for prediction results
- Displays predicted disease name and confidence score

---

## 🧪 Why Asynchronous Inference?

- Prevents API blocking during heavy model inference
- Supports concurrent users efficiently
- Matches **industry-standard ML microservice architectures**
- Enables independent scaling of workers and API layer

---

## 🛠️ Tech Stack

- **Deep Learning:** TensorFlow / Keras  
- **Backend:** FastAPI  
- **Async Tasks:** Celery  
- **Message Broker & Result Store:** Redis  
- **Reverse Proxy:** Nginx  
- **Containerization:** Docker & Docker Compose  
- **Frontend:** HTML, CSS, JavaScript  

---


## 🐳 Run the System

### Prerequisites
- Docker
- Docker Compose

### Start services
```
docker-compose up --build
```

### Access
- Frontend: http://localhost
- API Docs: http://localhost/docs

No virtual environment required.

---


## 👨‍💻 Author

**Arindam Das**  
Machine Learning / AI Engineer  

---
