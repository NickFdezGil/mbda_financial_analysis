import os

OWNER = 'unknown' # one, two, three, four, five, six
BASE_URL = "https://queuewars.luisbelloch.es"
# BASE_URL = "http://localhost:9000"
BOOTSTRAP_SERVERS = os.getenv('QUEUEWARS_BOOTSTRAP_SERVERS', 'localhost:29092')
