# Smart Retail Backend (FastAPI)

A modular, production-grade backend system for a smart retail environment that uses:

- YOLOv8 for real-time computer vision (product detection, customer movement)
- IoT sensor integration for tracking product interactions
- Blockchain (ERC-721 NFTs) for transparent billing and digital receipts
- AI/ML forecasting for warehouse inventory and restocking
- FastAPI as the high-performance backend framework

---

## Project Structure

smart-retail-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Entry point (FastAPI app)
│   ├── api/                     # All API route definitions
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── detect.py        # YOLO detection endpoints
│   │   │   ├── billing.py       # Checkout, NFT, payment
│   │   │   ├── inventory.py     # Stock, warehouse APIs
│   │   │   ├── kpi.py           # Dashboard metrics
│   │   │   └── iot.py           # IoT sensor data APIs
│   ├── core/                    # Core config, constants
│   │   ├── config.py            # Env vars, settings
│   │   └── logger.py            # Logging setup
│   ├── services/                # Business logic / external service wrappers
│   │   ├── yolo_service.py      # YOLOv8 logic (Ultralytics or custom)
│   │   ├── blockchain_service.py# Web3.py functions (NFT, billing)
│   │   ├── inventory_service.py # Restock prediction, shelf logic
│   │   └── iot_handler.py       # Sensor input validation
│   ├── models/                  # Pydantic models (schemas)
│   │   ├── __init__.py
│   │   ├── base.py              # Shared base schema
│   │   ├── detect.py
│   │   ├── billing.py
│   │   └── inventory.py
│   ├── db/                      # If using database (Postgres, Mongo)
│   │   ├── database.py
│   │   └── models.py            # SQLAlchemy or ODM models
│   ├── tasks/                   # Background tasks (Celery, APScheduler)
│   │   ├── __init__.py
│   │   └── retrain_model.py     # ML retraining, batch jobs
│   └── utils/                   # Utility functions
│       ├── file_ops.py
│       └── image_utils.py
├── scripts/                     # Helper scripts (data ingest, dev setup)
│   └── init_db.py
├── static/                      # Saved images, frames, logs
├── .env                         # Environment variables
├── requirements.txt
├── Dockerfile                   # Docker image setup
├── docker-compose.yml           # Optional: DB + app + inference
└── README.md


## Features

### AI Detection (YOLOv8)
- Detects customers and product interactions from video feeds
- Provides bounding boxes, object types, and confidence levels
- Powered by the Ultralytics YOLOv8 model

### Warehouse Automation
- Real-time stock updates from IoT devices
- ML-powered demand forecasting using Prophet or LSTM
- Inbound → Staging → Outbound process flow

### Checkout & Billing
- Auto-generates virtual cart based on product pickups
- Supports queue-less, cashless checkout
- Issues receipts as NFTs using `web3.py` and Ethereum-compatible contracts

### KPI Dashboard APIs
- Product-wise interactions
- Footfall analytics
- Checkout success rate
- Live stock level per zone

---

## Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Backend      | FastAPI (Python 3.10+) |
| AI Model     | YOLOv8 (Ultralytics)   |
| ML Forecast  | Prophet, Pandas, NumPy |
| Blockchain   | Web3.py, Solidity      |
| IoT Protocols| MQTT / REST            |
| Frontend     | Next.js                |
| Database     | PostgreSQL / Redis / MongoDB (optional) |

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Piyush22070/scan-n-go-ai-server.git
cd scan-n-go-ai-server


### 2.Create and Activate a Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### Install Dependencies
pip install -r requirements.txt


### Run the Application
uvicorn app.main:app --reload


### API Documentation
Once running, visit the following:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc