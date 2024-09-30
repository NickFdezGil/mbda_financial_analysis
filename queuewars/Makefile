TOPIC_NAME?=test

EXEC:=docker compose exec broker
BOOTSTRAP_SERVER:=--bootstrap-server broker:9092
KAFKA_TOPICS:=$(EXEC) kafka-topics $(BOOTSTRAP_SERVER)
KAFKA_CONSOLE_CONSUMER:=$(EXEC) kafka-console-consumer $(BOOTSTRAP_SERVER) --topic $(TOPIC_NAME)
KAFKA_CONSOLE_PRODUCER:=$(EXEC) kafka-console-producer $(BOOTSTRAP_SERVER) --topic $(TOPIC_NAME)

.PHONY: up
up:
	docker compose up

.PHONY: down
down:
	docker compose down --remove-orphans --rmi local --volumes

.PHONY: shell
shell:
	docker exec -it shell bash

.PHONY: ksqldb
ksqldb:
	docker exec -it ksqldb-cli ksql http://ksqldb-server:8088

.PHONY: up-ksqldb
up-ksqldb:
	docker compose -f docker-compose.yml -f docker-compose.ksqldb.yml up

.PHONY: down-ksqldb
down-ksqldb:
	docker compose -f docker-compose.yml -f docker-compose.ksqldb.yml down --remove-orphans --rmi local --volumes

.PHONY: up-cluster
up-cluster:
	docker compose -f docker-compose.yml -f docker-compose.cluster.yml up

.PHONY: down-cluster
down-cluster:
	docker compose -f docker-compose.yml -f docker-compose.cluster.yml down --remove-orphans --rmi local --volumes

.PHONY: create-topic list-topics delete-topic describe-topic producer producer-keys consumer consumer-keys consumer-from-beginning consumer-group describe-group create-topic-two-partitions consumer-partition-0 consumer-partition-1
create-topic:
	$(KAFKA_TOPICS) --create --topic $(TOPIC_NAME) --replication-factor 1 --partitions 1

list-topics:
	$(KAFKA_TOPICS) --list

delete-topic:
	$(KAFKA_TOPICS) --delete --topic $(TOPIC_NAME)

describe-topic:
	$(KAFKA_TOPICS) --describe --topic $(TOPIC_NAME)

producer:
	$(KAFKA_CONSOLE_PRODUCER)

producer-keys:
	$(KAFKA_CONSOLE_PRODUCER) --property parse.key=true --property key.separator=":"

consumer:
	$(KAFKA_CONSOLE_CONSUMER)

consumer-keys:
	$(KAFKA_CONSOLE_CONSUMER) --property print.key=true --property key.separator=":"

consumer-from-beginning:
	$(KAFKA_CONSOLE_CONSUMER) --from-beginning

consumer-group:
	$(KAFKA_CONSOLE_CONSUMER) --consumer-property group.id=work_queue_name

describe-group:
	$(EXEC) kafka-consumer-groups $(BOOTSTRAP_SERVER) --describe --group work_queue_name

create-topic-two-partitions:
	$(KAFKA_TOPICS) --create --topic $(TOPIC_NAME) --replication-factor 1 --partitions 2

consumer-partition-0:
	$(KAFKA_CONSOLE_CONSUMER) --from-beginning --partition 0

consumer-partition-1:
	$(KAFKA_CONSOLE_CONSUMER) --from-beginning --partition 1
