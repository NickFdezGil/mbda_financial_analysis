import json
import os

from confluent_kafka import Producer

# Documentation about Producers
# https://docs.confluent.io/kafka-clients/python/current/overview.html#ak-producer

def delivery_report(err, msg):
  if err is not None:
    print('ERROR: {}'.format(err))
  else:
    print('Delivered to topic "{}", paritition {}'.format(msg.topic(), msg.partition()))

topic_name = 'test'
bootstrap_servers = os.getenv('QUEUEWARS_BOOTSTRAP_SERVERS', 'broker:29092')
producer = Producer({ 'bootstrap.servers': bootstrap_servers })

message0 = json.dumps({ "id": 0, "has_no_key": True }).encode('utf-8')
producer.produce(topic_name, message0, callback=delivery_report)

message1 = json.dumps({ "id": 1, "animal": "penguin" }).encode('utf-8')
producer.produce(topic_name, message1, key="ABC", callback=delivery_report)

message2 = json.dumps({ "id": 2, "color": "blue" }).encode('utf-8')
producer.produce(topic_name, message2, key="DEF", callback=delivery_report)

message3 = json.dumps({ "id": 3, "animal": "lion" }).encode('utf-8')
producer.produce(topic_name, message3, key="ABC", callback=delivery_report)

producer.flush()

