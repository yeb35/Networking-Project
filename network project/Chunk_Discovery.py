import socket

serverFormat = "utf-8"
serverPort = 12000

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print('{} \n from {}'.format(message, clientAddress))
	#owner.json
	f = open("chunks.json", "w")
	f.write(message.decode(serverFormat))
	f.close()
	modifiedMessage = "Successfull"
	serverSocket.sendto(modifiedMessage.encode(serverFormat), clientAddress)