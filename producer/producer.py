import csv
import time
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open("../data/sample_transactions.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        data = {
            "user_id": int(row["user_id"]),
            "amount": float(row["amount"]),
            "timestamp": row["timestamp"]
        }
        producer.send("transactions", data)
        print("Sent:", data)
        time.sleep(1)

producer.flush()
