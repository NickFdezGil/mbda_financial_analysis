# Agora

This belongs to a workshop based on queues and NATS, and showcases basic usage of NATS queues and also a case study on a chat application.

## How to run it

1.  Start NATS in docker container:

```
docker run -p 4222:4222 -p 8222:8222 -p 6222:6222 -ti nats
```

That would expose NATS in port `4222`. If you want to use it across other containers, add the option `--network host` while running containers.

2.  Install dependencies

```
cd node
npm install
```

3.  Open two new terminals, start `gateway` and `persister` processes:

```
node gateway.js A
node gateway.js B
```

```
node persister.js 1
node persister.js 2
node persister.js 3
```

You might want to run those using docker. Make sure to include the option `--network host` or use a docker-compose file with a shared network between nodes.

```
docker run --network host -w /codigo -v "${PWD}"/node:/codigo -ti node:lts bash
yarn
node gateway.js A
```

## NATS 101

### Setup

Download NATS from http://nats.io, unpack it and run:

```
./gnatsd -m 8222
```

It enables two ports, `4222` for the procotol and `8222` with some small information site.

It can also be run via docker:

```
docker run -p 4222:4222 -p 8222:8222 -p 6222:6222 -ti nats:latest
```

### Protocol basics

Open two terminals, and telnet to port `4222`.

```
$ telnet localhost 4222
```

Then you can subscribe to messages sent to `foo.*`:

```
sub foo.* 90
```

Then try publishing some message from second terminal:

```
pub foo.bar 5
hello
```
