🚀 Production-Ready ML Inference System with A/B Testing

This repository implements a production-grade machine learning inference system designed for scalability, reliability, and controlled experimentation (A/B testing).

The system serves deep learning image classification models for Tomato Leaf Disease Detection using a Dockerized microservices architecture.

🧠 Key Features

✅ Versioned ML models (A/B testing ready)

✅ Asynchronous inference with Redis

✅ FastAPI-based REST API

✅ Background worker for model inference

✅ NGINX reverse proxy

✅ Docker & Docker Compose orchestration

✅ Frontend UI for image upload

✅ Separation of training & inference

✅ Production-safe model loading

🏗️ System Architecture
Client (Browser)
        │
        ▼
     NGINX
        │
        ▼
   FastAPI API
        │
        ▼
     Redis Queue
        │
        ▼
 Background Worker
        │
        ▼
   Versioned ML Model

📁 Project Structure
ml-inference-system/
│
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
├── Dockerfile.api           # FastAPI container
├── Dockerfile.worker        # Worker container
├── docker-compose.yml       # Multi-service orchestration
├── requirements.txt
└── README.md

🔀 Model Versioning & A/B Testing

Models are stored in versioned directories (v1, v2)

Same API endpoint can route traffic to different models

Enables:

Performance comparison

Accuracy vs latency trade-offs

Safe production experiments

Example loader:

load_model("v1")
load_model("v2")


👉 Model version is never exposed to frontend users

⚙️ How Inference Works

User uploads an image via UI or API

FastAPI enqueues request to Redis

Worker picks up the task asynchronously

Model performs inference

Prediction is returned to the user

This design:

Prevents API blocking

Supports concurrent requests

Scales horizontally

🌐 NGINX Reverse Proxy

NGINX:

Routes traffic to FastAPI

Acts as a single entry point

Enables future SSL / load balancing

location / {
    proxy_pass http://api:8000;
}

🐳 Dockerized Deployment
Why Docker?

Environment consistency

Easy scaling

Production-ready isolation

Services
Service	Purpose
api	Handles HTTP requests
worker	Performs ML inference
redis	Message queue
nginx	Reverse proxy
▶️ How to Run (Production Mode)
Prerequisites

Docker

Docker Compose

Start the system
docker-compose up --build

Access the app

Frontend: http://localhost

API: http://localhost/docs

❌ No virtual environment required
❌ No manual dependency installation

📦 Requirements
Python 3.10
TensorFlow
FastAPI
Redis
Uvicorn
Pillow
NumPy


All dependencies are handled inside Docker containers.

🔐 Production-Safe Design Decisions

compile=False when loading models

Background inference workers

Stateless API layer

Version-controlled models

No training code inside inference pipeline

📈 Performance & Scalability

Handles concurrent requests

Worker pool can be horizontally scaled

Redis ensures fault-tolerant task handling

Easily extendable to:

Kubernetes

Cloud deployment (AWS / GCP / Azure)

🧪 Training Pipeline

Training notebooks are intentionally separated from production inference code.

📂 See /training directory for:

Dataset link

Model architectures

Training details

Accuracy metrics

👨‍💻 Author

Arindam Das
Machine Learning / AI Engineer

This project demonstrates:

ML system design

Production deployment

A/B testing mindset

End-to-end ML ownership

⭐ Why This Project Matters

This is not just a CNN model.

It is a real-world ML system showing:

How models are served in production

How experiments are run safely

How ML meets DevOps