ML Inference System with A/B Testing

A production-ready machine learning inference system for image classification, built to demonstrate real-world ML deployment, asynchronous inference, and model A/B testing.

This project serves deep learning models for Tomato Leaf Disease Detection using a Dockerized microservices architecture.

What This Project Demonstrates

End-to-end ML system design (training → deployment)

Model versioning and A/B testing

Asynchronous inference using Redis

Scalable API + worker architecture

Production-grade Docker deployment

Architecture Overview
Client (Browser)
   ↓
NGINX (Reverse Proxy)
   ↓
FastAPI (API Layer)
   ↓
Redis (Task Queue)
   ↓
Worker (Inference)
   ↓
Versioned ML Models

Tech Stack
Layer	Technology
API	FastAPI
Inference	TensorFlow / Keras
Queue	Redis
Reverse Proxy	NGINX
Deployment	Docker, Docker Compose
Frontend	HTML, CSS
Repository Structure
ml-inference-system/
│
├── app/                 # FastAPI application
├── worker/              # Background inference worker
├── models/              # Versioned ML models (v1, v2)
├── templates/           # Frontend HTML
├── static/              # CSS assets
├── nginx/               # NGINX configuration
│
├── Dockerfile.api
├── Dockerfile.worker
├── docker-compose.yml
├── requirements.txt
└── README.md

Model Versioning & A/B Testing

Two independently trained CNN models:

v1 – 96% accuracy

v2 – 94% accuracy

Same architecture, different filter sizes

Traffic is dynamically routed to models

Model versions are not exposed to users

Purpose:

Compare accuracy vs inference behavior

Enable safe experimentation in production

Inference Flow

User uploads an image

API enqueues task to Redis

Worker processes inference

Prediction is returned asynchronously

Why this matters

API never blocks

Handles concurrent requests

Worker layer can scale independently

Running the System
Requirements

Docker

Docker Compose

Start all services
docker-compose up --build

Access

Web UI: http://localhost

API Docs: http://localhost/docs

No virtual environment setup required.

Training Details

Training is intentionally separated from inference.

Dataset: Kaggle Tomato Leaf Disease Dataset

Images: 18,345

Classes: 10

Optimizer: Adam

Loss: Sparse Categorical Crossentropy

Regularization:

Batch Normalization

Dropout

Early Stopping

Training notebooks are available in the training/ directory.

Production Design Decisions

Stateless API

Background inference workers

Redis-based task queue

compile=False for safe model loading

No training code in runtime containers

Scalability & Extensibility

Supports concurrent users

Horizontal scaling via workers

Kubernetes-ready architecture

Easily deployable to cloud platforms

Author

Arindam Das
Machine Learning / AI Engineer

This project showcases practical ML system design beyond model training.

Why This Project

Most ML projects stop at accuracy.

This one shows:

How models are served

How experiments are run safely

How ML systems scale in production
