# 🚀 Production-Ready ML Inference System with A/B Testing

This repository implements a production-grade machine learning inference system designed for scalability, reliability, and controlled experimentation (A/B testing). 

The system serves deep learning image classification models for **Tomato Leaf Disease Detection** using a Dockerized microservices architecture.

---

## 🧠 Key Features

* ✅ **Versioned ML models**: Ready for A/B testing and seamless rollouts.
* ✅ **Asynchronous inference**: Powered by Redis to handle heavy workloads without blocking.
* ✅ **FastAPI-based REST API**: High-performance interface for model interaction.
* ✅ **Background Worker**: Dedicated processing for model inference logic.
* ✅ **NGINX Reverse Proxy**: Single entry point for security and load balancing.
* ✅ **Docker Orchestration**: Fully containerized using Docker Compose.
* ✅ **Frontend UI**: Simple interface for user-friendly image uploads.
* ✅ **Production-Safe Design**: Separation of training and inference logic.

---

## 🏗️ System Architecture



```text
Client (Browser) 
      │ 
      ▼ 
    NGINX (Reverse Proxy)
      │ 
      ▼ 
   FastAPI (API Layer) 
      │ 
      ▼ 
   Redis (Task Queue) 
      │ 
      ▼ 
 Background Worker (Inference Engine)
      │ 
      ▼ 
 Versioned ML Models (H5/SavedModel)
