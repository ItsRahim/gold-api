from kafka import KafkaProducer
import json
import yaml

from models import gold_model

with open('app/config/kafka_config.yaml', 'r') as kafka_config_file:
    kafka_config = yaml.safe_load(kafka_config_file)['kafka']


def get_kafka_producer():
    KAFKA_SERVER = kafka_config['bootstrap_servers']

    kafka_producer = KafkaProducer(
        bootstrap_servers=[KAFKA_SERVER],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    return kafka_producer


def send_price_kafka(gold: gold_model):
    PRODUCER_TOPIC = kafka_config['topic']
    message = json.dumps(gold.to_dict())

    kafka_producer = get_kafka_producer()
    kafka_producer.send(PRODUCER_TOPIC, message)
