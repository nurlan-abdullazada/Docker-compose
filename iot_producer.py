from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Kafka configuration
bootstrap_servers = ['localhost:9094', 'localhost:9095', 'localhost:9096']

# Create producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None,
    retries=5
)

# IoT sensors
sensors = [
    {"id": "sensor_001", "location": "Baku_Central", "type": "temperature"},
    {"id": "sensor_002", "location": "Baku_Port", "type": "humidity"},
    {"id": "sensor_003", "location": "Ganja_Industrial", "type": "temperature"}
]

def generate_sensor_data():
    sensor = random.choice(sensors)
    
    if sensor["type"] == "temperature":
        value = round(random.uniform(-5, 45), 2)
        unit = "°C"
    elif sensor["type"] == "humidity":
        value = round(random.uniform(20, 95), 2)
        unit = "%"
    
    return {
        "sensor_id": sensor["id"],
        "location": sensor["location"],
        "sensor_type": sensor["type"],
        "value": value,
        "unit": unit,
        "timestamp": datetime.now().isoformat()
    }

print("Starting IoT Data Generator...")
message_count = 0

try:
    while True:
        data = generate_sensor_data()
        key = data["sensor_id"]
        
        producer.send('iot-sensors', key=key, value=data)
        
        message_count += 1
        print(f"Sent message {message_count}: {data}")
        
        time.sleep(2)  # Wait 2 seconds between messages
        
except KeyboardInterrupt:
    print(f"Stopping. Sent {message_count} messages.")
finally:
    producer.close()
