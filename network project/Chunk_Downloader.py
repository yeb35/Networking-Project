import socket

c = socket.socket()
q = "localhost"
p = 1905
condition = True
s = input("Enter the file name you want to download : ")
c.connect((q,p))
f = open("Downloads/"+s+".png","wb")
while condition:
    image = c.recv(1024)
    if str(image) == "b''":
        condition = False
    f.write(image)
#Log_Downloads