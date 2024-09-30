import asyncio
import signal

from datetime import datetime

from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def main():
  nc = NATS()
  await nc.connect(servers=["nats://127.0.0.1:4222"])

  await nc.publish("foo.thing", b'Hello!')
  message = 'Current date: at {now}'.format(now=datetime.now().isoformat())
  await nc.publish("foo.bar", message.encode())

if __name__ == '__main__':
  asyncio.run(main())
