# -*- coding:utf-8 -*-

import sys
import websocket
import time

ws = websocket.WebSocket()
ws.connect("ws://localhost:8765", max_size = 10752000)

#ws.send("Hello world audio")
#txtAnswer = ws.recv_frame()
time.sleep(2)
file = open(sys.argv[1], 'rb')
content = file.read()
#print(content)
ws.send_binary(content)
file.close()

#ws.send_binary([100, 220, 130])
#ws.send_binary("\xdc\x82aaaaaaa")
#binAnswer = ws.recv_frame()
#print(binAnswer.data)

#print("----BINARY---")
#print (websocket.ABNF.OPCODE_MAP[binAnswer.opcode])

#for byte in bytearray(binAnswer.data):
#J    print(byte)

#ws.send("Hello world")
txtAnswer = ws.recv_frame()
print( websocket.ABNF.OPCODE_MAP[txtAnswer.opcode])
#tmp = unicode(txtAnswer.data,'utf-8').encode('gbk')
print(txtAnswer.data.decode("utf-8"))

ws.close()
