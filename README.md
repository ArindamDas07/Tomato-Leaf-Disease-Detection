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
 Versioned ML Models (H5/SavedModel
 
📁 Project StructurePlaintextml-inference-system/
│
├── app/                    # FastAPI application
│   ├── main.py             # API endpoints
│   ├── model.py            # Versioned model loader
│   ├── preprocess.py       # Image preprocessing
│   ├── tasks.py            # Task enqueue logic
│   └── redis_conn.py       # Redis connection
│
├── worker/                 # Background inference worker
│   └── worker.py
│
├── models/                 # Versioned ML models
│   ├── v1/
│   │   └── Tomato_model_v1.h5
│   └── v2/
│       └── Tomato_model_v2.h5
│
├── templates/              # Frontend UI
│   └── index.html
│
├── static/                 # CSS/JS Assets
│   └── style.css
│
├── nginx/                  # Reverse proxy configuration
│   └── nginx.conf
│
├── Dockerfile.api          # FastAPI container definition
├── Dockerfile.worker       # Worker container definition
├── docker-compose.yml      # Multi-service orchestration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

🔀 Model Versioning & A/B TestingModels are stored in versioned directories (v1, v2). The system allows routing traffic to different model versions to enable:
       Performance comparison in real-world scenarios.
       Accuracy vs. Latency trade-off analysis.
       Safe experiments without exposing internal versioning to the end-user.

Example Internal Loader:
model_v1 = load_model("models/v1/Tomato_model_v1.h5")
model_v2 = load_model("models/v2/Tomato_model_v2.h5")


⚙️ How Inference WorksUpload:
       User uploads an image via the UI or API.
       Enqueue: FastAPI receives the file and enqueues a task into Redis.
       Process: The Worker picks up the task, performs preprocessing, and runs inference.
       Result: The prediction result is returned asynchronously or stored for retrieval.
       Benefits: Prevents API timeouts, supports high concurrency, and allows horizontal scaling of workers.


🌐 NGINX Reverse ProxyNGINX acts as the gateway, routing traffic to the internal API and serving as a foundation for future SSL termination and load balancing.

Nginx
location / {
    proxy_pass http://api:8000;
}

🐳 Dockerized Deployment
Service,Purpose
api,Handles HTTP requests and task delegation.
worker,Performs heavy ML inference.
redis,Acts as the message broker (Queue).
nginx,Reverse proxy and static file server.


▶️ How to Run
Prerequisites: Docker & Docker Compose installed.
   1. Clone the repo
   2. Start the system:
            docker-compose up --build

   3. Access the application:
           Frontend: http://localhost
           API Docs: http://localhost/docs


🔐 Production-Safe Design Decisions
        compile=False: Used during model loading to save memory and avoid training overhead.
        Decoupled Architecture: Training code is kept strictly separate from the inference pipeline.
        Statelessness: The API layer can be scaled infinitely as it holds no state.


👨‍💻 Author
Arindam Das - Machine Learning / AI Engineer
This project demonstrates expertise in ML System Design, Production Deployment, and an End-to-End Ownership mindset.


⭐ If you find this project useful, please consider giving it a star!

