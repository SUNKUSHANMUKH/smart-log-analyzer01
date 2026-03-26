# 🧠 Smart Log Analyzer & Alert System

> An AI-powered DevOps project that automatically analyzes application logs, detects anomalies, and sends alerts — deployed on Kubernetes with full CI/CD automation.

![Project Banner](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

---

## 📖 Table of Contents

- [What This Project Does](#-what-this-project-does)
- [Architecture Overview](#-architecture-overview)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Phase 1 — Project Setup & Docker](#-phase-1--project-setup--docker)
- [Phase 2 — AI Log Analyzer](#-phase-2--ai-log-analyzer)
- [Phase 3 — Kubernetes Deployment](#-phase-3--kubernetes-deployment)
- [Phase 4 — Terraform](#-phase-4--terraform)
- [Phase 5 — Jenkins CI/CD](#-phase-5--jenkins-cicd)
- [Phase 6 — Monitoring with Prometheus & Grafana](#-phase-6--monitoring-with-prometheus--grafana)
- [API Endpoints](#-api-endpoints)
- [Common Errors & Fixes](#-common-errors--fixes)
- [Project Structure](#-project-structure)
- [What You Learn](#-what-you-learn)

---

## 🎯 What This Project Does

Most applications generate thousands of log lines every second:

```
ERROR: Database connection timeout after 30s
CRITICAL: Service crashed unexpectedly
WARNING: High memory usage detected — 87% used
INFO: User login successful
```

Manually watching these logs is impossible at scale. This project **automates log monitoring using AI**:

1. A **FastAPI app** simulates a real backend service generating logs
2. **Groq AI (LLaMA 3)** reads each log and responds with severity, root cause, and recommended action
3. Everything runs inside **Kubernetes** — self-healing, scalable, production-ready
4. **Jenkins** automatically deploys every code change
5. **Prometheus + Grafana** provide real-time visual dashboards

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Your Laptop                          │
│                                                         │
│  ┌─────────────┐    ┌──────────────┐                   │
│  │   Jenkins   │───▶│ Docker Build │                   │
│  │  (CI/CD)    │    └──────┬───────┘                   │
│  └─────────────┘           │                           │
│                             ▼                           │
│  ┌──────────────────────────────────────────────────┐  │
│  │              Minikube (Kubernetes)               │  │
│  │                                                  │  │
│  │  ┌─────────────┐    ┌─────────────────────────┐ │  │
│  │  │  FastAPI App │───▶│   Groq AI Analyzer      │ │  │
│  │  │  (2 replicas)│    │   (LLaMA 3 model)       │ │  │
│  │  └─────────────┘    └─────────────────────────┘ │  │
│  │                                                  │  │
│  │  ┌─────────────┐    ┌──────────────────────────┐│  │
│  │  │ Prometheus  │───▶│       Grafana            ││  │
│  │  │ (metrics)   │    │    (dashboards)          ││  │
│  │  └─────────────┘    └──────────────────────────┘│  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │         Terraform (manages K8s resources)       │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Tool | Purpose | Free? |
|------|---------|-------|
| **Python + FastAPI** | Backend app that generates logs | ✅ Yes |
| **Docker** | Package app into containers | ✅ Yes |
| **Minikube** | Run Kubernetes locally on your laptop | ✅ Yes |
| **Kubernetes (kubectl)** | Orchestrate and manage containers | ✅ Yes |
| **Groq API** | Free AI API (LLaMA 3 model) for log analysis | ✅ Free tier |
| **Jenkins** | CI/CD — auto build & deploy on code push | ✅ Yes |
| **Terraform** | Infrastructure as Code for K8s resources | ✅ Yes |
| **Prometheus** | Collect app metrics | ✅ Yes |
| **Grafana** | Visualize metrics on dashboards | ✅ Yes |
| **Helm** | Kubernetes package manager | ✅ Yes |

> ⚠️ **No AWS, no cloud account needed.** Everything runs 100% locally.

---

## ✅ Prerequisites

### System Requirements
- macOS, Linux, or Windows (WSL2 recommended for Windows)
- Minimum 8GB RAM (16GB recommended)
- 20GB free disk space
- Stable internet connection for initial setup

### Accounts Needed
- [GitHub](https://github.com) — free account
- [Groq Console](https://console.groq.com) — free account for AI API key

### Install These Tools First

**1. Docker Desktop**
```bash
# Download from: https://www.docker.com/products/docker-desktop/
# After installing, verify:
docker --version
# Expected: Docker version 24.x.x or higher
```

**2. Minikube**
```bash
# macOS
brew install minikube

# Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Verify
minikube version
```

**3. kubectl**
```bash
# macOS
brew install kubectl

# Linux
sudo apt-get install -y kubectl

# Verify
kubectl version --client
```

**4. Terraform**
```bash
# macOS
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

# Linux
sudo apt-get install -y terraform

# Verify
terraform --version
```

**5. Helm**
```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify
helm version
```

**6. Python 3.10+**
```bash
python3 --version
# Expected: Python 3.10.x or higher
```

---

## 🚀 Phase 1 — Project Setup & Docker

### Step 1.1 — Clone or Create the Project

```bash
# Create project folder
mkdir smart-log-analyzer && cd smart-log-analyzer

# Create all required folders
mkdir -p app ai_analyzer k8s terraform jenkins monitoring tests
```

### Step 1.2 — Create the FastAPI Application

```bash
cat > app/main.py << 'EOF'
from fastapi import FastAPI
import random
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/simulate")
def simulate_logs():
    events = [
        "INFO: User login successful",
        "ERROR: Database connection timeout after 30s",
        "WARNING: High memory usage detected — 87% used",
        "CRITICAL: Service crashed unexpectedly",
        "INFO: API request processed in 120ms",
    ]
    log = random.choice(events)
    logging.info(log)
    return {"log": log}
EOF
```

### Step 1.3 — Create requirements.txt

```bash
cat > requirements.txt << 'EOF'
fastapi
uvicorn
groq
prometheus-fastapi-instrumentator
EOF
```

### Step 1.4 — Create the Dockerfile

> ⚠️ **Important:** The CMD must use `app.main:app` because your file is at `app/main.py` and WORKDIR is `/app`. This is the most common beginner mistake.

```bash
cat > dockerfile << 'EOF'
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF
```

### Step 1.5 — Build & Test Locally with Docker

```bash
# Build the image
docker build -t smart-log-app:v1 .

# Run it locally to verify it works BEFORE touching Kubernetes
docker run --rm -p 8000:8000 smart-log-app:v1
```

Open a **new terminal tab** and test:

```bash
curl http://localhost:8000/
# Expected: {"status":"running"}

curl http://localhost:8000/simulate
# Expected: {"log":"INFO: User login successful"}
```

> ✅ **Checkpoint:** If you see responses above, Docker is working. Stop the container with Ctrl+C and move to Phase 2.

---

## 🤖 Phase 2 — AI Log Analyzer

### Step 2.1 — Get Your Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Click **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_...`)

> ⚠️ **Never commit API keys to GitHub.** We will use Kubernetes secrets to store them safely.

### Step 2.2 — Create the AI Analyzer

```bash
cat > ai_analyzer/analyzer.py << 'EOF'
import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def analyze_log(log_text: str) -> str:
    prompt = f"""
    You are a DevOps expert. Analyze this log entry and respond ONLY in JSON format:
    Log: {log_text}

    Return exactly this structure:
    {{
        "severity": "LOW or MEDIUM or HIGH or CRITICAL",
        "issue": "brief description of what went wrong",
        "action": "what the engineer should do",
        "alert_needed": true or false
    }}
    """
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    log = "CRITICAL: Database connection timeout after 30s"
    print(analyze_log(log))
EOF
```

### Step 2.3 — Test the AI Analyzer Locally

```bash
pip install groq
export GROQ_API_KEY="your_groq_key_here"
python ai_analyzer/analyzer.py
```

Expected output:
```json
{
  "severity": "CRITICAL",
  "issue": "Database is unreachable, connections are timing out",
  "action": "Check database server status, verify network connectivity, review connection pool settings",
  "alert_needed": true
}
```
### if you faced any issue with installation of python 
```json
#Go with Homebrew: 
brew install python

Or download from python.org

#Install the groq package with the correct pip
pip3 install groq

#Set the API key (again, if needed)
export GROQ_API_KEY="your_groq_key_here"

#Run the script again
python3 ai_analyzer/analyzer.py
```

### facing issue with LLM model  


model="llama-3.1-8b-instant",   # change the model to this

```json
export GROQ_API_KEY="your_groq_key_here"
python3 ai_analyzer/analyzer.py
```

### Step 2.4 — Add AI Endpoint to FastAPI

Add this to `app/main.py`:

```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai_analyzer.analyzer import analyze_log

@app.get("/analyze")
def analyze():
    events = [
        "ERROR: Database connection timeout after 30s",
        "CRITICAL: Pod OOMKilled — memory limit exceeded",
        "WARNING: API response time 5000ms, threshold 1000ms",
    ]
    log = random.choice(events)
    analysis = analyze_log(log)
    return {"log": log, "ai_analysis": analysis}
```

---

## ☸️ Phase 3 — Kubernetes Deployment

### Step 3.1 — Start Minikube

```bash
minikube start --driver=docker
```
```
# Verify it's running
minikube status
kubectl get nodes
```
Expected output:
```
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

### Step 3.2 — CRITICAL: Build Image Inside Minikube

> ⚠️ **This is the most important step beginners miss.** Minikube has its own Docker daemon separate from your Mac/Linux Docker. If you build on your machine, Minikube can't see the image.

```bash
# Point your terminal's Docker to Minikube's Docker daemon
eval $(minikube docker-env)

# Now rebuild — this goes into Minikube's registry
docker build -t smart-log-app:v1 .

# Verify Minikube can see it
minikube image ls | grep smart-log-app
```

### Step 3.3 — Create Kubernetes Secret for API Key

```bash
kubectl create secret generic groq-secret \
  --from-literal=api-key=YOUR_GROQ_API_KEY        # you need keep your apikey here

```
if you face with the secret key creation 
```
kubectl delete secret groq-secret
kubectl create secret generic groq-secret --from-literal=api-key=type_YOUR_NEW_API_KEY  
```

# Verify it was created
kubectl get secrets
```

### Step 3.4 — Create Kubernetes Deployment

```bash
cat > k8s/deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: log-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: log-app
  template:
    metadata:
      labels:
        app: log-app
    spec:
      containers:
      - name: log-app
        image: smart-log-app:v1
        imagePullPolicy: Never
        ports:
        - containerPort: 8000
        env:
        - name: GROQ_API_KEY
          valueFrom:
            secretKeyRef:
              name: groq-secret
              key: api-key
        - name: GROQ_MODEL
          value: "llama-3.1-8b-instant"
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: log-app-service
spec:
  selector:
    app: log-app
  ports:
  - port: 80
    targetPort: 8000
  type: NodePort
EOF
```

### Step 3.5 — Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml

# Watch pods come up (takes ~30 seconds)
kubectl get pods -w
```

Expected output:
```
NAME                      READY   STATUS    RESTARTS   AGE
log-app-xxxxxxxx-xxxxx    1/1     Running   0          30s
log-app-xxxxxxxx-xxxxx    1/1     Running   0          30s
```

> ✅ **Checkpoint:** Both pods show `1/1 Running`. If you see `CrashLoopBackOff`, check the [Common Errors](#-common-errors--fixes) section.

### Step 3.6 — Access Your App

```bash
# This command gives you a URL — keep this terminal open
minikube service log-app-service --url
```

Open a **new terminal tab** and use the URL printed above:

```bash
curl http://127.0.0.1:PORT/
curl http://127.0.0.1:PORT/simulate
curl http://127.0.0.1:PORT/analyze
```

### Step 3.7 — Useful Kubernetes Commands

```bash
# See all running resources
kubectl get all

# View logs from your pods
kubectl logs -l app=log-app

# Scale to 3 replicas
kubectl scale deployment log-app --replicas=3

# Update to a new version
docker build -t smart-log-app:v2 .
kubectl set image deployment/log-app log-app=smart-log-app:v2
kubectl rollout status deployment/log-app

# Open the Kubernetes dashboard
minikube dashboard

# Roll back if something breaks
kubectl rollout undo deployment/log-app
```
### If you face any issues
```
dont stop the process that is going on the terminal
open new terminal and do this on it!!!
Automatically you will see the browser will be open and you can the K8's cluster, pods and everything
```

### Step-by-step fix
## 1. Verify your FastAPI code has the /analyze endpoint
Look at your local app.py (or whichever file you copied into the image). It should contain:
```
python
@app.get("/analyze")
def analyze():
    # ... your logic
```
If it’s missing, add it and save.

### 2. Connect to Minikube’s Docker daemon
You must build the image inside Minikube’s Docker, so Kubernetes can pull it without a registry.

```
eval $(minikube docker-env)
```
Verify it worked:

```
docker info | grep "Server Version"
```
You should see a version that matches Minikube’s Docker.

### 3. Build the new image with the updated code
```
docker build -t smart-log-app:v2 .
```
(If you get permission errors, try sudo or ensure your user is in the docker group.)



---

## 🏗️ Phase 4 — Terraform

### Step 4.1 — Create Terraform Configuration

```bash
cat > terraform/main.tf << 'EOF'
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "log_system" {
  metadata {
    name = "log-system"
  }
}

resource "kubernetes_deployment" "log_app" {
  metadata {
    name      = "log-app-tf"
    namespace = kubernetes_namespace.log_system.metadata[0].name
  }
  spec {
    replicas = 2
    selector {
      match_labels = { app = "log-app" }
    }
    template {
      metadata {
        labels = { app = "log-app" }
      }
      spec {
        container {
          name  = "log-app"
          image = "smart-log-app:v1"
          image_pull_policy = "Never"
          port {
            container_port = 8000
          }
        }
      }
    }
  }
}
EOF

cat > terraform/variables.tf << 'EOF'
variable "replicas" {
  description = "Number of pod replicas"
  type        = number
  default     = 2
}
EOF

cat > terraform/outputs.tf << 'EOF'
output "namespace" {
  value = kubernetes_namespace.log_system.metadata[0].name
}
EOF
```

### Step 4.2 — Run Terraform

```bash
cd terraform

# Initialize (download providers) — run once
terraform init

# Preview what will be created
terraform plan

# Create the resources
terraform apply

# Type 'yes' when prompted

# See what was created
terraform show

# When done, clean up
terraform destroy
# Type 'yes' what to destory
```

---

## 🔧 Phase 5 — Jenkins CI/CD

### Step 5.1 — Start Jenkins

```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts

# Get the initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Open [http://localhost:8080](http://localhost:8080) and complete setup.

### Step 5.2 — Create the Jenkinsfile

```bash
cat > Jenkinsfile << 'EOF'
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'smart-log-app'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_USERNAME/smart-log-analyzer'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest tests/ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl set image deployment/log-app log-app=${IMAGE_NAME}:${IMAGE_TAG}"
                sh "kubectl rollout status deployment/log-app"
            }
        }

        stage('Verify') {
            steps {
                sh 'kubectl get pods'
            }
        }
    }

    post {
        success { echo '✅ Deployment Successful!' }
        failure  { echo '❌ Build Failed — Check logs!' }
    }
}
EOF
```

### Step 5.3 — Set Up Jenkins Pipeline

1. Open Jenkins at [http://localhost:8080](http://localhost:8080)
2. Click **New Item** → **Pipeline**
3. Under **Pipeline**, select **Pipeline script from SCM**
4. Set SCM to **Git** and enter your GitHub repo URL
5. Set **Script Path** to `Jenkinsfile`
6. Click **Save** then **Build Now**

---

## 📊 Phase 6 — Monitoring with Prometheus & Grafana

### Step 6.1 — Add Metrics to FastAPI

Add to `app/main.py`:

```python
from prometheus_fastapi_instrumentator import Instrumentator

# Add this right after app = FastAPI()
Instrumentator().instrument(app).expose(app)
```

Your app now exposes metrics at `/metrics` automatically.

### Step 6.2 — Install Prometheus + Grafana via Helm

```bash
# Add the Helm chart repository
helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts
helm repo update

# Install the full monitoring stack
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace

# Wait for all pods to be ready (takes 2-3 minutes)
kubectl get pods -n monitoring -w
```

### Step 6.3 — Access Dashboards

**Grafana Dashboard:**
```bash
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
```
Open [http://localhost:3000](http://localhost:3000)
- Username: `admin`
- Password: `prom-operator`

**Prometheus:**
```bash
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n monitoring
```
Open [http://localhost:9090](http://localhost:9090)

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check — returns `{"status": "running"}` |
| `GET` | `/simulate` | Generate a random log entry |
| `GET` | `/analyze` | Generate a log + AI analysis |
| `GET` | `/metrics` | Prometheus metrics endpoint |

---

## 🐛 Common Errors & Fixes

### CrashLoopBackOff
```bash
# Always check logs first
kubectl logs -l app=log-app

# Common causes:
# 1. Wrong module path → use app.main:app in Dockerfile CMD
# 2. Missing packages → check requirements.txt
# 3. App crashes on startup → test with docker run first
```

### Could not import module "main"
```
Cause: Dockerfile CMD uses wrong module path
Fix:   Change CMD to ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### ImagePullBackOff
```bash
# Cause: Minikube can't find the image
# Fix 1: Build inside Minikube's Docker
eval $(minikube docker-env)
docker build -t smart-log-app:v1 .

# Fix 2: Or load an existing image
minikube image load smart-log-app:v1
```

### Secret not found
```bash
# Recreate the secret
kubectl delete secret groq-secret
kubectl create secret generic groq-secret --from-literal=api-key=YOUR_KEY
kubectl rollout restart deployment/log-app
```

### Service not found after kubectl delete all --all
```bash
# kubectl delete all --all deletes services too!
# Recreate it:
kubectl expose deployment log-app \
  --type=NodePort \
  --port=80 \
  --target-port=8000 \
  --name=log-app-service
```

### zsh: command not found: #
```
Cause: Pasting commands with # comments directly into zsh
Fix:   Run commands ONE AT A TIME, never paste comment blocks
```

### Nuclear Reset — When Everything Is Broken
```bash
kubectl delete all --all
kubectl delete secret --all
minikube stop
minikube delete
minikube start --driver=docker
eval $(minikube docker-env)
docker build -t smart-log-app:v1 .
kubectl create secret generic groq-secret --from-literal=api-key=YOUR_KEY
kubectl apply -f k8s/deployment.yaml
```

---

Your pods are stuck in `ErrImageNeverPull` because the image `smart-log-app:v1` is not present in Minikube's Docker daemon. You already ran `eval $(minikube docker-env)` and then `docker images` showed no matching image, confirming it’s missing.

Part 1: Fix the ErrImageNeverPull (Minikube Side)
Before moving to Jenkins, let's get your actual application running.

1. Point Terminal to Minikube
This ensures your docker build command sends the image directly into Minikube’s internal registry.

```
eval $(minikube docker-env)
```
2. Build the Image inside Minikube
Run this from your project root (where the Dockerfile is):

```
docker build -t smart-log-app:v1 .
```
3. Verify and Restart
Confirm the image is visible to Minikube, then force Kubernetes to try pulling it again.

```
# Verify image presence
docker images | grep smart-log-app

# Force a restart of the pods
kubectl rollout restart deployment/log-app

# Watch them turn green (Running)
kubectl get pods -w
```
Part 2: Setup Jenkins (Host Side)

Now that the app is healthy, let’s get your CI/CD server running on your host machine.
1. Reset Environment for Host Docker
Crucial: You must disconnect from Minikube’s Docker env so Jenkins runs on your Mac/PC, not inside the cluster.

```
eval $(minikube docker-env -u)
```
2. Launch Jenkins
We mount the Docker socket so Jenkins can build images for you later.
```
docker rm -f jenkins 2>/dev/null
docker run -d \
  -p 9090:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts
```
3. Get the Unlock Key

sleep 30
```
docker logs jenkins 2>&1 | grep -A 2 "Please use the following password"
```
Action: Go to http://localhost:9090 and paste the code found in the logs.

Part 3: Secrets & Testing

1. Inject the API Key
If your app uses Groq for AI analysis, the pod needs the secret to exist in the cluster.

```
kubectl create secret generic groq-secret \
  --from-literal=api-key=YOUR_ACTUAL_GROQ_KEY \
  --dry-run=client -o yaml | kubectl apply -f -
```
2. Test the API
Bridge the Minikube network to your localhost:
```
kubectl port-forward service/log-app-service 8080:80 &
curl http://localhost:8080/analyze
```

Troubleshooting Table
Symptom	Cause	Quick Fix
ErrImageNeverPull	Image built on Host, not Minikube.	Run eval $(minikube docker-env) then rebuild.
Jenkins Offline	Docker Desktop daemon stopped.	Restart Docker Desktop and check docker ps.
Connection Refused	Port-forwarding died.	Re-run the kubectl port-forward command.
Pod Crash (Auth)	Missing groq-secret.	Check kubectl get secrets.



---
## 📁 Project Structure

```
smart-log-analyzer/
├── app/
│   └── main.py                  # FastAPI application
├── ai_analyzer/
│   └── analyzer.py              # Groq AI log analysis
├── k8s/
│   └── deployment.yaml          # Kubernetes Deployment + Service
├── terraform/
│   ├── main.tf                  # Terraform config
│   ├── variables.tf             # Input variables
│   └── outputs.tf               # Output values
├── jenkins/
│   └── Jenkinsfile              # CI/CD pipeline definition
├── monitoring/
│   └── grafana-dashboard.json   # Grafana dashboard config
├── tests/
│   └── test_main.py             # Unit tests
├── dockerfile                   # Container build instructions
├── requirements.txt             # Python dependencies
├── .gitignore                   # Files to exclude from git
└── README.md                    # This file
```

---

## 💡 What You Learn

By completing this project you will understand:

| Skill | Where You Learn It |
|-------|-------------------|
| **Docker** | Building images, writing Dockerfiles, testing containers locally |
| **Kubernetes** | Pods, deployments, services, secrets, scaling, rolling updates |
| **Debugging K8s** | Using kubectl logs, describe, exec to diagnose issues |
| **AI/LLM Integration** | Calling Groq API, prompt engineering, parsing responses |
| **Jenkins** | Setting up pipelines, writing Jenkinsfiles, automating deployments |
| **Terraform** | Writing HCL, init/plan/apply/destroy workflow, IaC concepts |
| **Prometheus** | Instrumenting apps, scraping metrics, writing queries |
| **Grafana** | Building dashboards, visualizing time-series data |
| **FastAPI** | Building REST APIs with Python |
| **Git Workflow** | Committing, pushing, branching, pull requests |

---

## 🔐 Security Best Practices

- ✅ Never hardcode API keys — always use Kubernetes secrets
- ✅ Add `.env` and `*.key` files to `.gitignore`
- ✅ Rotate API keys immediately if accidentally committed
- ✅ Use `imagePullPolicy: Never` for local development
- ✅ Limit resource requests/limits in production deployments

---

## 📚 Resources

- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [Minikube Getting Started](https://minikube.sigs.k8s.io/docs/start/)
- [Groq API Docs](https://console.groq.com/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Terraform Kubernetes Provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs)
- [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)

---

## 🙌 Author

Built as a learning project covering DevOps fundamentals + AI integration.
Feel free to fork, improve, and make it your own!

---

> *"Every error you hit and fix makes you a better engineer. The hours spent debugging teach you more than weeks of reading docs."*
