from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "fraud_alerts",
    bootstrap_servers = "localhost:29092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: m.decode("utf-8")
)

print("Listening for fraud alerts...\n")

for msg in consumer:
    print(msg.value)
