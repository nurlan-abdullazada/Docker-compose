from kafka import KafkaConsumer
import json

# Kafka configuration
bootstrap_servers = ['localhost:9094', 'localhost:9095', 'localhost:9096']

# Create consumer
consumer = KafkaConsumer(
    'iot-sensors',
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    group_id='iot-consumer-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

print("Starting IoT Consumer...")
print("Listening for messages... Press Ctrl+C to stop")
print("-" * 50)

message_count = 0

try:
    for message in consumer:
        message_count += 1
        
        sensor_data = message.value
        sensor_id = message.key
        partition = message.partition
        offset = message.offset
        
        print(f"Message #{message_count}")
        print(f"Key: {sensor_id}")
        print(f"Partition: {partition}, Offset: {offset}")
        print(f"Data: {sensor_data}")
        print("-" * 30)
        
except KeyboardInterrupt:
    print(f"Stopped. Processed {message_count} messages.")
finally:
    consumer.close()
