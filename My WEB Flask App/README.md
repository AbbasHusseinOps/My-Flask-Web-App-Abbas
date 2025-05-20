# 🧮 Flask + Redis Visit Counter App

A clean, containerized web app that tracks visits using Flask and Redis — built and orchestrated entirely with Docker.

---

## 🚀 Project Overview

This project demonstrates my ability to:

- ✅ Build backend services with Python & Flask
- ✅ Integrate Redis for data persistence
- ✅ Use Docker Compose for multi-container architecture
- ✅ Write readable, production-style code with clean documentation

---

## 🛠 Tech Stack

| Technology | Role |
|------------|------|
| 🐍 Python (Flask) | Web framework |
| 🔴 Redis | Visit counter store |
| 🐳 Docker | Containerization |
| 📦 Docker Compose | Multi-service orchestration |

---

## 🌐 App Functionality

| Route      | Description                      |
|------------|----------------------------------|
| `/`        | Displays a welcome message       |
| `/count`   | Increments & returns visit count |

---

## 🧪 How to Run Locally

**Step 1:** Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed.  
**Step 2:** Clone the repo, then run:

```bash
docker compose up --build
Visit the app in your browser:

🔗 http://localhost:5003
🔗 http://localhost:5003/count
To stop the app:

bash
Copy
Edit
Ctrl+C
docker compose down
📁 Project Structure

bash
Copy
Edit
├── app.py               # Flask web app
├── Dockerfile           # Flask container build
├── docker-compose.yml   # Orchestrates Flask + Redis
├── requirements.txt     # Python dependencies
└── README.md            # You're here!
