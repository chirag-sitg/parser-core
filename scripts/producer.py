from kafka import KafkaProducer
import json
from parser_core.config import kafka_broker, kafka_coupon_parser_queue_via_api

producer = KafkaProducer(bootstrap_servers=kafka_broker(), value_serializer=lambda m: json.dumps(m).encode('ascii'))

def push_to_kafka(requestDto):
    kafka_topic = kafka_coupon_parser_queue_via_api()
    requestJson = json.dumps(requestDto.__dict__)
    print(requestJson)
    producer.send(kafka_topic, json.loads(requestJson))
