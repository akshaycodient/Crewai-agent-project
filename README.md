# Project Name :- CREWAI-AGENT-PROJECT

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)


---

## Project Overview

web-based dashboard that interacts with Grist, triggers a workflow in n8n, and utilizes an AI agent via CrewAI to analyze or process the data. The goal is to simulate a real-world integration scenario involving API communication, Python scripting, and a lightweight Vue.js frontend.


---

## Features

### 📊 Grist Integration (Data Source)
- Dynamic customer issue table with fields: *ID, **Customer Name, **Issue Description, **Status*
- RESTful API access to fetch and update issue records
- Real-time data visibility from Grist to the dashboard

### 🔁 n8n Workflow Automation
- Webhook-based workflow triggered from the frontend
- Fetches issue data from Grist via API
- Logs or processes data through custom nodes (e.g., dummy endpoint or email)
- Fully extendable for more advanced automation (e.g., notification, Slack integration)

### 🧠 CrewAI Agent (AI-Powered Issue Classification)
- Python-based CrewAI agent built with *FastAPI*
- Uses *OpenAI's GPT model* (or compatible local LLM) to classify issues into:
  - Bug
  - Feature Request
  - Other
- Simple API endpoint for classification, integrated with the frontend

### 🌐 Vue.js Dashboard (Frontend)
- Clean and minimal interface to:
  - View all customer issues
  - Trigger n8n workflow per issue
  - Classify issues using AI agent with one click
- Shows AI-classified category inline with each record
- Axios-powered REST communication with backend services

### 🧩 Modular & Extensible Architecture
- Decoupled components: Grist, n8n, AI, and Frontend can evolve independently
- Easy to plug in new workflows, models, or data sources
- Can be extended into a full-featured support ticketing system or internal tool

---

## Tech Stack

- **Backend**: [FastAPI]
- **Frontend**: [Vue.js]
- **Database**: [Grist]
- **AI agent**: [CrewAI]
- **AI agent**: [CrewAI]
- **LLM Model**: [huggingface : facebook/bart-large-mnli]

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [List any software that needs to be installed]
	- Node.js
	- Python


---

## Installation

To set up and run the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/akshaycodient/Crewai-agent-project.git
   ```

2. **Install Backend Dependencies** (For Python projects)

   If you’re using Python, install the required dependencies via `pip`:

   ```bash
   pip install -r requirements.txt
   ```


3. **Install Frontend Dependencies** (For JS projects)

   If you have a frontend, navigate to the frontend directory and install the dependencies:

   ```bash
   cd vue-dashboard
   npm install
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory add the following variables:

   ```bash
   GRIST_API_KEY=grist api key
   GRIST_DOC_ID=grist doc id
   N8N_WEBHOOK_URL =    LLM_TASK = Task name of choice
   LLM_MODEL=LLM model of choice
   ```

   Ensure all necessary environment variables are added based on your project’s requirements.

---

## Usage

To start the backend server, run the following command:

### Backend (FastAPI Example):

```bash
cd .\backend\ 
uvicorn main:app --reload --port 5000

OR
uvicorn backend.main:app --reload --port 5000

```

If you are using a frontend, you can run it separately:

### Frontend (React Example):

```bash
npm run dev
```

Now, open your browser and visit `http://localhost:5173/` (or another URL if you're using a different configuration).

FOR Testing Backend API you can access them via API docs :- `http://127.0.0.1:5000/docs#`

---

## Folder Structure

Here’s an overview of the folder structure in the project:

```
project/
│
├── backend/                 # Backend application
│   ├── main.py              # Main FastAPI app
│   ├── crewai_agent.py      # crewai configuration
│   ├── grist_client.py      # grist doc configuration with access method
│ 
│
├── vue-dashboard/            # Frontend application
│   ├── src/                  # Source files
│   ├── public/               # Static files
│   ├── package.json          # Frontend dependencies
│   ├── package-lock.json     # Frontend package dependencies
│   └── vite.config.js        # frontend api configurations 
│
└── .env                     # Environment variables
│
└── requirements.txt         # Project dependencies
```

---


### Notes:
As we are using open source LLM model(hugging-face) check the installation Prerequisites for torch and transformer setup with your system
Let me know if you need further adjustments!