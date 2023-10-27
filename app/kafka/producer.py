from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from app.config.logging import log
import json

from app.models import gold
from app.config.load_config import load_config

config = load_config('kafka')


def get_kafka_producer():
    KAFKA_SERVER = config['bootstrap_servers']

    kafka_producer = KafkaProducer(
        bootstrap_servers=[KAFKA_SERVER],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    return kafka_producer


def send_price_kafka(data: gold):
    PRODUCER_TOPIC = config['topic']
    message = json.dumps(data.to_dict())

    kafka_producer = get_kafka_producer()
    try:
        kafka_producer.send(PRODUCER_TOPIC, message)
        log.info(f"Sent message to Kafka topic: {PRODUCER_TOPIC}")
    except Exception as e:
        log.error(f"Failed to send message to Kafka: {e}")


def initialise():
    KAFKA_SERVER = config['bootstrap_servers']
    TOPIC_NAME = config['topic']
    NUM_PARTITIONS = 3
    REPLICATION_FACTOR = 1

    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER)
    new_topic = NewTopic(TOPIC_NAME, num_partitions=NUM_PARTITIONS, replication_factor=REPLICATION_FACTOR)

    admin_client.create_topics([new_topic])
    log.info(f"Kafka topic '{TOPIC_NAME}' created successfully.")