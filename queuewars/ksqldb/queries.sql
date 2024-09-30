CREATE STREAM prices (
  timestamp VARCHAR,
  symbol VARCHAR,
  close DOUBLE,
  high DOUBLE,
  low DOUBLE,
  open DOUBLE,
  volume DOUBLE
) WITH (
  kafka_topic='prices',
  value_format='json',
  partitions=1,
  timestamp = 'timestamp',
  timestamp_format = 'yyyy-MM-dd'
);

INSERT INTO prices (timestamp, symbol, close, high, low, open, volume)
VALUES ('2020-04-22', 'AAPL', 30.1046, 30.4786, 30.08, 30.4443, 0);

SET 'auto.offset.reset' = 'earliest';

SELECT ROWTIME, * FROM prices EMIT CHANGES;

SELECT symbol, MIN(close) / MAX(close) - 1 AS PCT_CHANGE, MIN(close) T0, MAX(close) T1
FROM prices
WINDOW HOPPING (SIZE 2 DAYS, ADVANCE BY 1 DAYS)
GROUP BY symbol
EMIT CHANGES;

DROP STREAM payments DELETE TOPIC;

CREATE STREAM payments (
  payment_id VARCHAR KEY,
  payment_status VARCHAR,
  amount DOUBLE
) WITH (value_format='JSON', partitions=1, kafka_topic='payments');

CREATE TABLE payment_status AS
SELECT
  payment_id,
  LATEST_BY_OFFSET(payment_status) AS last_status,
	COUNT(*) AS num_of_events
FROM payments
GROUP BY payment_id
EMIT CHANGES;

INSERT INTO payments VALUES ('MIT001', 'initiated', 45.2);
INSERT INTO payments VALUES ('MIT002', 'initiated', 12.1);
INSERT INTO payments VALUES ('MIT001', 'delivered', 32.4);
INSERT INTO payments VALUES ('STF001', 'initiated', 78.6);
INSERT INTO payments VALUES ('MIT002', 'delivered', 94.5);
INSERT INTO payments VALUES ('STF002', 'initiated', 67.9);

SELECT * FROM payment_status;
