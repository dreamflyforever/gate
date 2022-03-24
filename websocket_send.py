# -*- coding:utf-8 -*-

import sys
import websocket
import time

ws = websocket.WebSocket()
ws.connect("ws://localhost:8765", max_size = 10752000)

ws.send("Hello world test")
#txtAnswer = ws.recv_frame()
time.sleep(2)

with open(sys.argv[1], 'rb') as f:
    while True:
        content = f.read(3200)
        if not content:
            break
        ws.send_binary(content)

ws.send(' ')

print("receive....")
txtAnswer = ws.recv_frame()
print( websocket.ABNF.OPCODE_MAP[txtAnswer.opcode])
#tmp = unicode(txtAnswer.data,'utf-8').encode('gbk')
print(txtAnswer.data.decode("utf-8"))

ws.close()
