import os
import requests
from dotenv import load_dotenv

load_dotenv()

GRIST_API_KEY = os.getenv("GRIST_API_KEY")
GRIST_DOC_ID = os.getenv("GRIST_DOC_ID")

def fetch_grist_records():
    headers = {"Authorization": f"Bearer {GRIST_API_KEY}"}
    url = f"https://docs.getgrist.com/api/docs/{GRIST_DOC_ID}/tables/Table1/records"
    response = requests.get(url, headers=headers)
    return response.json()
