# 🍅 Scalable Tomato Disease Detection: A/B Testing & Drift-Aware MLOps

**Author:** Arindam Das  

**Full Project Bundle (Ready-to-Run with Models):** 🚀 Download from Google Drive  
https://drive.google.com/file/d/161i7iTkMNj74_E_RX0BA_Sbg-ZRmxkZJ/view?usp=drive_link 

---

## 1. 📝 Project Overview

This project is an end-to-end Computer Vision MLOps system. It transitions from deep learning research into a Production-Grade Infrastructure capable of handling high-velocity image inference with automated data validation and system monitoring.

### 🌟 Key MLOps Features:

- 🛡️ Multi-Stage Pipeline: Features a lightweight MobileNetV2 Gatekeeper that filters out non-tomato images, reducing heavy classification costs by ~60%.
- ⚖️ Production A/B Testing: Implements weighted random routing (70/30) between EfficientNetB0 (Challenger) and ResNet50 (Champion) to compare performance in real-time.
- 📉 Automated Data Drift Tracking: Monitors Brightness, Contrast, and RGB channels of every live upload against a baseline of 18,339 training samples.
- ⚡ Decoupled Scaling: A lightweight FastAPI gateway (no-ML build) handles ingestion, while heavy inference is distributed across independent Celery workers.

---

## 2. 🧬 Machine Learning & Research

### 🧠 Model Performance (Test Set)

| Stage | Model | Accuracy | Role |
|------|-------|----------|------|
| Stage 1 | MobileNetV2 | 100% | Binary Gatekeeper (Filter) |
| Stage 2 | EfficientNetB0 | 96.0% | High-speed Challenger |
| Stage 2 | ResNet50 | 96.3% | High-stability Champion |

### 📊 Training Data Baseline (The "Source of Truth")

The system calculates real-time drift using these pre-computed metrics from the training set:

Mean Brightness: 116.53 | Mean Contrast: 44.83  
Mean Red: 118.48 | Mean Green: 121.47 | Mean Blue: 109.64

---

## 3. 🏗️ System Architecture

### 🗺️ System Flow Diagram

```text
User (Browser / Client)
        ↓
Nginx (Reverse Proxy, Load Balancer & Rate Limiter) 🛡️
        ↓
FastAPI API Replicas (Stateless Ingestor - Lightweight) ⚡
        ↓ (Writes to Shared Volume /app/uploads)
Redis (Task Queue - DB 0) 📩
        ↓
Celery Worker Pool (Distributed Inference Nodes) 🧠
  ├─ Stage 1: Gatekeeper (MobileNetV2 Filter)
  ├─ If Valid: Calculate Data Drift vs. Training Baseline
  └─ Stage 2: A/B Routing (70% EfficientNet / 30% ResNet)
        ↓ (Logs Metrics)
MLflow🧪 | Prometheus📈 | Grafana🎨 | Pushgateway📮
        ↓
User Receives Result (Disease Name + Confidence) ✅
```

### 🛡️ Infrastructure Wins (Advanced Production Engineering)

Strict Decoupling: The API image is stripped of TensorFlow, reducing its RAM footprint from 1.2GB to ~70MB per instance.

Zero-Copy Handover: Uses Docker shared volumes for image transfer, preventing Redis memory bloat.

Dynamic Service Discovery: Nginx uses a dynamic DNS resolver (127.0.0.11) to prevent 502 errors during horizontal scaling.

Storage Hygiene: Ephemeral workspaces are automatically purged via shutil.rmtree after each completed transaction.

---

## 4. 👁️ Full-Stack Observability

The system tracks both the AI's Brain and the Server's Health.

🧪 MLflow: Logs per-request traces including drift percentages, model confidence, and model variant for audit trails.

📈 Prometheus: Tracks request volume, filter rejection rates, and hardware health.

📮 Pushgateway: Handles metric collection from ephemeral background workers.

🎨 Grafana: Provides a visual dashboard for P95 Latency and environmental drift alerts.

---

## 5. 💻 How to Run

### 📥 One-Click Deployment

Download and unzip the bundle from the Google Drive link above.

Open a terminal in the root folder.

Run:

```bash
docker-compose up --build -d --scale api=3 --scale worker=2
```

---

## 🔗 Monitoring Endpoints

🌍 Main Application: http://localhost

📊 API Telemetry: http://localhost/metrics

🧪 MLflow Dashboard: http://localhost:5000

📡 Prometheus UI: http://localhost:9090

🎨 Grafana Dashboard: http://localhost:3000

📮 Pushgateway UI: http://localhost:9091

---

## 🚀 Scalability & Roadmap

This architecture is Cloud-Native and ready for Kubernetes. By separating the gateway from the inference nodes, workers can be scaled onto dedicated GPU clusters while the API remains on low-cost CPU instances.

---

Arindam Das  
Master’s in Electronics & Telecommunication  
ML / AI / MLOps Engineer
