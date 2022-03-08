#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import asyncio
import websockets
import websocket as ws
import logger
import os

main = r"./fos"

async def hello(websocket):
    name = await websocket.recv()
    if "audio" in f"{name}":
        print(name)
    else:
        t = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        file = open(t, 'wb')
        file.write(name)
        file.close()
        rv=os.popen("./fos %s" % (t))
        answer = rv.read()
        print(answer)
        await websocket.send(answer)

async def main():
    async with websockets.serve(hello, "localhost", 8765, max_size = 10752000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
