import json

from confluent_kafka import Consumer

consumer = Consumer({
  'bootstrap.servers': 'broker:9092',
  'group.id': 'work_queue_name',
  'auto.offset.reset': 'earliest' # 'latest'
})

topic_name = 'prices'
consumer.subscribe([topic_name])

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

consumer.close()
