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

async def gate(websocket):
    while True:
        name = await websocket.recv()
        if name == ' ':
            print("receive end flag");
            break;
        if "test" in f"{name}":
            t = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
            print(name)
            file = open(t, 'wb')
        else:
            file.write(name)

    print("send result....")
    rv=os.popen("./fos %s" % (t))
    answer = rv.read()
    print(answer)
    await websocket.send(answer)
    client.publish(topic, answer)
    file.close()

async def main():
    async with websockets.serve(gate, "localhost", 8765, max_size = 10752000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    client = connect_mqtt()
    asyncio.run(main())
