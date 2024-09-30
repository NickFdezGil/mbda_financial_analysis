import asyncio
import signal

from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def main():
  nc = NATS()

  async def closed_cb():
    print("Connection to NATS is closed.")
    await asyncio.sleep(0.1)
    asyncio.get_running_loop().stop()

  options = {
    "servers": ["nats://127.0.0.1:4222"],
    "closed_cb": closed_cb
  }

  await nc.connect(**options)
  print("Connected to NATS at {}...".format(nc.connected_url.netloc))

  async def message_handler(msg):
    subject = msg.subject
    reply = msg.reply
    data = msg.data.decode()
    print("{subject} [{reply}]: {data}".format(
      subject=subject, reply=reply, data=data))

  await nc.subscribe("foo.*", cb=message_handler)

  def signal_handler():
    if nc.is_closed:
      return
    print("Disconnecting...")
    asyncio.create_task(nc.close())

  for sig in ('SIGINT', 'SIGTERM'):
    asyncio.get_running_loop().add_signal_handler(getattr(signal, sig), signal_handler)

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  try:
    loop.run_forever()
  finally:
    loop.close()
