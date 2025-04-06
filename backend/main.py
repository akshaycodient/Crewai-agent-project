import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crewai_agent import classify_issue
from grist_client import fetch_grist_records
import requests
from dotenv import load_dotenv

load_dotenv()

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for input
class Issue(BaseModel):
    description: str


# Trigger n8n
def trigger_n8n(customer_name: str, description: str, category: str):
    try:
        requests.post(N8N_WEBHOOK_URL, json={
            "customer": customer_name,
            "description": description,
            "category": category
        })
    except Exception as e:
        print("Error triggering n8n:", e)

@app.get("/grist-data")
def get_data():
    return fetch_grist_records()

@app.post("/classify")
def classify(issue: Issue):
    category = classify_issue(issue.description)
    trigger_n8n("Unknown", issue.description, category)
    return {"category":category}
