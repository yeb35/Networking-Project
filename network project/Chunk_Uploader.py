import socket
import json

f = open('chunks.json',"r")
data = json.load(f)
f.close()

c = 0
q1 = "localhost"
q2 = 1905
s = socket.socket()
s.bind((q1,q2))
s.listen(1)
c,address = s.accept()
for j in range(0,5):
    image = open("Chunks/"+data["chunks"][j],"rb")
    if c != 0:
        for i in image:
            c.send(i)
    print(j)

#Log_Uploader