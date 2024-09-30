import json
import os

from confluent_kafka import Consumer, OFFSET_BEGINNING, TopicPartition

# Documentation about Consumers
# https://docs.confluent.io/kafka-clients/python/current/overview.html#ak-consumer

consumer = Consumer({
  'bootstrap.servers': os.getenv('QUEUEWARS_BOOTSTRAP_SERVERS', 'broker:29092'),
  'group.id': 'work_queue_name',
  'enable.auto.commit': True,
  'auto.offset.reset': 'earliest' # 'latest'
})

topic_name = 'test'
consumer.subscribe([topic_name])

# Listen to only one specific partition
# consumer.assign([TopicPartition(topic_name, 2)])

# Consume from beginning of the topic
# def reset_offset(consumer, partitions):
#   print("consumer", consumer, "partitions", partitions)
#   for p in partitions:
#     p.offset = OFFSET_BEGINNING
#   consumer.assign(partitions)

# consumer.subscribe([topic_name], on_assign=reset_offset)

try:
  while True:
    message = consumer.poll(1.0)

    if message is None:
      continue
    if message.error():
      print("ERROR: {}".format(message.error()))
      continue

    message_as_text = message.value().decode('utf-8')
    message_as_json = json.loads(message_as_text)

    print('Received: {}'.format(message_as_text))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
