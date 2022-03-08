#!/usr/bin/env python

import time
import asyncio
import websockets
import websocket as ws
import logger
import os
from paho.mqtt import client as mqtt_client
import random

main = r"./fos"

broker = '127.0.0.1'
port = 1883
topic = "mqtt"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

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
        client.publish(topic, answer)

async def main():
    async with websockets.serve(hello, "localhost", 8765, max_size = 10752000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    client = connect_mqtt()
    asyncio.run(main())
