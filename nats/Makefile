BUCKET_NAME:=bigdata.luisbelloch.es
COMMIT_ID=$(shell git log --pretty=format:'%h' -n 1)
OUT=build
PKG=$(OUT)/agora-$(COMMIT_ID).tar.gz
PKG_SOLVED=$(OUT)/agora-solved-$(COMMIT_ID).tar.gz

.PHONY: release
release: clean $(PKG) $(PKG_SOLVED)

.PHONY: clean
clean:
	rm -rf $(OUT)

$(OUT):
	mkdir -p $(OUT)

$(PKG): $(OUT)
	git archive --worktree-attributes --format=tar HEAD . | gzip -9 > $(PKG)

$(PKG_SOLVED): $(PKG)
	git archive --format=tar HEAD . | gzip -9 > $(PKG_SOLVED)

.PHONY: nats
nats:
	docker run -p 4222:4222 -p 8222:8222 -p 6222:6222 -ti nats:latest

.PHONY: push
push: $(PKG)
	gsutil -h "Cache-Control:no-cache,max-age=0" cp $(PKG) gs://${BUCKET_NAME}/nats.tgz
	gsutil -h "Cache-Control:no-cache,max-age=0" cp $(PKG_SOLVED) gs://${BUCKET_NAME}/nats-solved.tgz
