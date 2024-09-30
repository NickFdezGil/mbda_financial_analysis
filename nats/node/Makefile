IMAGE_NAME:=luisbelloch/agora

.PHONY: shell
shell:
	docker run --network host -v $(PWD):/app -w /app -ti node:lts bash

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: push
push:
	docker push $(IMAGE_NAME)
