# app.py
import sys
import os
import random
import logging
from fastapi import FastAPI

# Add the parent directory to the path to import from ai_analyzer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai_analyzer.analyzer import analyze_log

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Root endpoint
@app.get("/")
def home():
    return {"status": "running"}

# Simulate random log generation
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

# Analyze a random log using the AI analyzer
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

# Run with: uvicorn app:app --reload (if executed directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)