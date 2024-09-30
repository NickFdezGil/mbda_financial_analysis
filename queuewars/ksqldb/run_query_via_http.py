import requests

payload = {
  'ksql': "SELECT ROWTIME, * FROM prices LIMIT 10;",
  'streamsProperties': { 'ksql.streams.auto.offset.reset': 'earliest' }
}
r = requests.post('http://localhost:8088/query', json=payload)

print("status:", r.status_code)
print("body:", r.text)

# Run through the shell container
# docker exec -ti shell python ksqldb/run_query_via_http.py
# r = requests.post('http://ksqldb-server:8088/query', json=payload)
