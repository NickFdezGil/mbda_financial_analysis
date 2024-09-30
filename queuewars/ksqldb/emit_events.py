import csv
import json

from confluent_kafka import Producer

def delivery_report(err, msg):
  if err is not None:
    print('\nERROR: {}'.format(err))
  else:
    print('.', end='')

topic_name = 'prices'
producer = Producer({'bootstrap.servers': 'broker:9092'})
# producer = Producer({'bootstrap.servers': 'localhost:9092'})

with open('aapl.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  next(reader)
  for date, close, high, low, open, volume in reader:
    event = { "TIMESTAMP": date, "SYMBOL": "AAPL", "CLOSE": close, "HIGH": high, "LOW": low, "OPEN": open, "VOLUME": volume }
    message = json.dumps(event).encode('utf-8')
    producer.produce(topic_name, message, callback=delivery_report)

producer.flush()
print("\n")
