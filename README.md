# Real-Time Fraud Detection System using Kafka & Faust

A complete real-time fraud detection pipeline built using **Apache Kafka**, **Faust Stream Processing**, and **Python**.  
This system simulates financial transactions, detects suspicious activity, and publishes alerts for downstream consumers.

---

##  Project Overview

This project demonstrates how streaming financial data can be analyzed in real-time to detect fraud.  

The system includes:

- **Producer** → sends transactions from CSV  
- **Faust Processor** → applies fraud rules  
- **Consumer** → listens for fraud alerts  
- **Kafka Cluster** (Confluent Platform) via Docker Compose  

---

##  Architecture
- CSV → Producer → Kafka Topic (transactions)
- ↓
- Faust Processor
- (applies fraud detection rules)
- ↓
- Kafka Topic (fraud_alerts)
- ↓
- Python Consumer


**Confluent components included:**

- Kafka Broker  
- Zookeeper  
- Schema Registry  
- Kafka Connect  
- Control Center  

---

##  Tech Stack

| Component | Technology |
|----------|------------|
| Stream Messaging | Apache Kafka |
| Stream Processing | Faust |
| Deployment | Docker Compose |
| Programming Language | Python 3.9 |
| Serialization | JSON |
| Monitoring | Confluent Control Center |

---

##  Folder Structure

- fraud-detection/
- │
- ├── docker-compose.yml
- │
- ├── data/
- │ └── sample_transactions.csv
- │
- ├── producer/
- │ └── producer.py
- │
- ├── processor/
- │ └── fraud_processor.py
- │
- ├── consumer/
- │ └── consumer.py



---

##  Fraud Detection Logic

###  Rule 1 — High-Value Transaction
Triggers an alert when:
amount > 700


###  Rule 2 — Rapid Transactions
Triggers an alert if the user performs **3 transactions within the last 5 events**.

---

##  Running the System

### Start Kafka Cluster
```bash
docker compose up -d
Kafka → localhost:29092
Control Center → http://localhost:9021
Schema Registry → http://localhost:8081
Kafka Connect → http://localhost:8083

---

---

