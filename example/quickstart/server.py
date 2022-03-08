#!/usr/bin/env python

import time
import asyncio
import websockets
import websocket as ws
import logger

async def hello(websocket):
    name = await websocket.recv()
    if "audio" in f"{name}":
        print(name)
    else:
        print("binary")
        file = open(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'wb')
        file.write(name)
        file.close()

    #greeting = f"Hello {name}!"

    #await websocket.send(greeting)
    #print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, "localhost", 8765, max_size = 10752000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
