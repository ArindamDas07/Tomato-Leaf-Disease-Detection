Production-Ready ML Inference System with A/B Testing

This repository contains a production-grade machine learning inference system for image classification, designed with scalability, reliability, and experimentation (A/B testing) in mind.

The system serves deep learning models for Tomato Leaf Disease Detection using a Dockerized microservices architecture, following real-world ML deployment practices.

Overview

Problem
Deploy deep learning models in a way that supports:

.Concurrent users

.Asynchronous inference

.Model versioning and experimentation

.Clean separation between training and production

Solution
A containerized inference system using:

.FastAPI for request handling

.Redis for task queuing

.Background workers for inference

.NGINX as a reverse proxy

.Versioned ML models for A/B testing

Key Features

.Versioned ML models (v1, v2) for A/B testing

.Asynchronous inference using Redis

.FastAPI-based REST API

.Background worker architecture (non-blocking)

.Docker & Docker Compose for deployment

.NGINX reverse proxy

.Web UI for image upload and prediction

.Clear separation of training and inference code

.Production-safe model loading

System Architecture
Client (Browser)
        |
        v
      NGINX
        |
        v
   FastAPI API
        |
        v
   Redis Task Queue
        |
        v
 Background Worker
        |
        v
   Versioned ML Model
   

Project Structure
ml-inference-system/
│
├── app/                     # FastAPI application
│   ├── main.py              # API routes and request handling
│   ├── model.py             # Versioned model loader
│   ├── preprocess.py        # Image preprocessing logic
│   ├── tasks.py             # Redis task enqueue logic
│   ├── redis_conn.py        # Redis connection configuration
│
├── worker/                  # Background inference service
│   └── worker.py
│
├── models/                  # Versioned trained models
│   ├── v1/
│   │   └── Tomato_model_v1.h5
│   └── v2/
│       └── Tomato_model_v2.h5
│
├── templates/               # Frontend HTML
│   └── index.html
│
├── static/                  # Frontend styling
│   └── style.css
│
├── nginx/                   # Reverse proxy configuration
│   └── nginx.conf
│
├── Dockerfile.api           # FastAPI container
├── Dockerfile.worker        # Worker container
├── docker-compose.yml       # Multi-service orchestration
├── requirements.txt
└── README.md


Model Versioning & A/B Testing

.Models are stored in versioned directories (v1, v2)

.Traffic can be split between models programmatically

.Enables safe experimentation without impacting users

.Model version is never exposed to the frontend

Example:

load_model("v1")
load_model("v2")



This design allows:

.Accuracy comparison

.Architecture experimentation

.Controlled production rollout


Inference Workflow

1.User uploads an image via the UI or API

2.FastAPI enqueues the request to Redis

3.Background worker processes the task

4.Model performs inference

5.Prediction (disease + confidence score) is returned

Why this matters:

API remains responsive

Supports concurrent requests

Scales independently of inference workload

NGINX Reverse Proxy

NGINX serves as the entry point to the system:

Routes traffic to FastAPI

Decouples client access from internal services

Enables future SSL, rate limiting, or load balancing

Example configuration:

location / {
    proxy_pass http://api:8000;
}

Dockerized Deployment
Why Docker?

Environment consistency

Reproducible builds

Production isolation

Easy scaling

Services
Service	Responsibility
api	Handles HTTP requests
worker	Performs model inference
redis	Task queue
nginx	Reverse proxy
Running the System
Prerequisites

Docker

Docker Compose

Start all services
docker-compose up --build

Access

Web UI: http://localhost

API docs: http://localhost/docs

No virtual environment setup is required.
All dependencies are handled inside containers.

Production Design Considerations

Models loaded with compile=False

Stateless API layer

Asynchronous task processing

Version-controlled models

Training code excluded from runtime inference

Performance & Scalability

Supports concurrent inference requests

Workers can be scaled horizontally

Redis provides fault-tolerant task handling

Architecture is Kubernetes-ready

Cloud deployable (AWS / GCP / Azure)

Training Pipeline

Model training is deliberately separated from inference.

The training directory includes:

Dataset source

Training notebooks

Architecture details

Accuracy metrics

This ensures production code remains clean and lightweight.

Author

Arindam Das
Machine Learning / AI Engineer

This project demonstrates:

End-to-end ML system design

Production deployment practices

Model experimentation via A/B testing

Strong separation of concerns between training and serving

Why This Project Matters

This repository goes beyond model training.

It demonstrates how machine learning systems are:

Deployed in production

Scaled under load

Experimented safely

Integrated with real infrastructure
