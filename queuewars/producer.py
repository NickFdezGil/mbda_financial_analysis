import json
import api

# PRODUCER
# Goals: read N chunks, publish them on queue
# Decide:
# - 1 or N topics
# - 1 or N partitions per topic
# - Consumer groups?

def main():
  chunks = api.fetch()
  for chunk in chunks:
    print('Chunk', chunk)

if __name__ == '__main__':
  main()
