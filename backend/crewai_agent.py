import os
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

LLM_TASK = os.getenv("LLM_TASK")
LLM_MODEL = os.getenv("LLM_MODEL")

# classifier = pipeline(LLM_TASK, model=LLM_MODEL)
classifier = pipeline('zero-shot-classification', model="facebook/bart-large-mnli")

CATEGORIES = ["Bug", "Feature Request", "Other"]

def classify_issue(issue_description: str) -> str:
    result = classifier(issue_description, CATEGORIES)
    return result["labels"][0]
