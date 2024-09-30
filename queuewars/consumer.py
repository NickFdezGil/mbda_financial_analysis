import api

from confluent_kafka import Consumer

# CONSUMER
# Goals: read from queue, confirm when sum = 1
# Decide:
# - 1 or N topics
# - 1 or N partitions per topic
# - Consumer groups?

def main():
  # TODO Check sum equals 1, then send the whole block
  # Each block might have variable number of chunks
  # To confirm block, use api.confirm
  parent = 42
  chunk_ids = ['99f4e8', '656cfc', '8b346a', '788ea0', 'bf238a']
  statusCode = api.confirm(parent, chunk_ids)
  if statusCode == 200:
    print("Confirmed block", parent)
  else:
    print("Block", parent, "was not valid")

if __name__ == '__main__':
   main()

