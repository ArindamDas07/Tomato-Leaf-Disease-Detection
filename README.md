
# 🍅 ML Inference System with A/B Testing

A **production-ready machine learning inference system** for image classification, demonstrating **real-world ML deployment**, **asynchronous inference**, and **model A/B testing**.

This project serves deep learning CNN models for **Tomato Leaf Disease Detection** using a **Dockerized microservices architecture**.

---

## 🚀 Key Highlights

- End-to-end ML system (training → deployment)
- Model versioning & A/B testing
- Asynchronous inference with Redis
- Scalable FastAPI + Worker architecture
- Docker & Docker Compose deployment
- Frontend UI for image upload & prediction

---

## 🏗️ System Architecture

```
Client (Browser)
   ↓
NGINX (Reverse Proxy)
   ↓
FastAPI (API Layer)
   ↓
Redis (Task Queue)
   ↓
Background Worker
   ↓
Versioned ML Models
```

---

## 🧰 Tech Stack

| Layer        | Technology |
|-------------|------------|
| API         | FastAPI |
| ML          | TensorFlow / Keras |
| Queue       | Redis |
| Proxy       | NGINX |
| Deployment  | Docker, Docker Compose |
| Frontend    | HTML, CSS |

---

## 📁 Project Structure

```
ml-inference-system/
├── app/                     # FastAPI application
│   ├── main.py              # API endpoints
│   ├── model.py             # Versioned model loader
│   ├── preprocess.py        # Image preprocessing
│   ├── tasks.py             # Task enqueue logic
│   ├── redis_conn.py        # Redis connection
│
├── worker/                  # Background inference worker
│   └── worker.py
│
├── models/                  # Versioned ML models
│   ├── v1/
│   │   └── Tomato_model_v1.h5
│   └── v2/
│       └── Tomato_model_v2.h5
│
├── templates/               # Frontend UI
│   └── index.html
│
├── static/
│   └── style.css
│
├── nginx/                   # Reverse proxy
│   └── nginx.conf
│
├── Dockerfile.api
├── Dockerfile.worker
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔀 Model Versioning & A/B Testing

- Two independently trained CNN models
- Same architecture, different filter sizes
- **v1 Accuracy:** 96%
- **v2 Accuracy:** 94%
- Traffic is split dynamically
- Model version is never exposed to users

---

## ⚙️ Inference Flow

1. Image uploaded via UI or API
2. FastAPI enqueues request to Redis
3. Worker performs inference asynchronously
4. Prediction & confidence returned

✔ Non-blocking API  
✔ Concurrent request handling  
✔ Horizontally scalable workers  

---

## 🌐 NGINX Reverse Proxy

- Acts as a single entry point
- Routes traffic to FastAPI
- Ready for SSL & load balancing

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

## 🧪 Training Pipeline

- Kaggle Tomato Leaf Disease Dataset
- 18,345 images
- 10 disease classes

### Model Design
- CNN
- Batch Normalization
- Dropout
- Early Stopping

```
Optimizer: Adam
Loss: SparseCategoricalCrossentropy
Metrics: Accuracy
```

Training notebooks are included separately.

---

## 🔐 Production Design Choices

- Stateless API
- Background workers
- Redis task queue
- Safe model loading (compile=False)
- Training separated from inference

---

## 📈 Scalability

- Handles concurrent users
- Worker-based horizontal scaling
- Kubernetes-ready
- Cloud deployable

---

## 👨‍💻 Author

**Arindam Das**  
Machine Learning / AI Engineer  

---

## ⭐ Why This Project Matters

This is not just a CNN model.

It demonstrates:
- Production ML deployment
- A/B testing mindset
- ML + DevOps integration
- Real-world system design
