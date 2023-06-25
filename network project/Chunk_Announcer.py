import os
import math
import socket
import json
import time


def Prepare_Chunk(file_path):
    filename = file_path+'.png'
    c = os.path.getsize(filename)
    #print(c)
    CHUNK_SIZE = math.ceil(math.ceil(c)/5) 
    #print(CHUNK_SIZE)
    index = 1
    with open(filename, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
        while chunk:
            chunkname = file_path+'_'+str(index)
            #print("chunk name is: " + chunkname + "\n")
            with open("Chunks/"+chunkname,'wb+') as chunk_file:
                # with open("Chunks/"+chunkname,'wb+') as chunk_file:
                chunk_file.write(chunk)
            index += 1
            chunk = infile.read(int(CHUNK_SIZE))
    print("Chunks are ready.")
    chunk_file.close()

serverFormat = "utf-8"
serverIP = 'localhost'
serverPort = 12000
server_address = (serverIP, serverPort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def Announcer():

    path = os.getcwd() + "/" + "Chunks"
    files = os.listdir(path)
    python_dict = {"chunks" : files}
    json_dict = json.dumps(python_dict)
    print("Announcing..")

    clientSocket.sendto(json_dict.encode(serverFormat), server_address)

    modifiedMessage, server = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode("utf-8"))

    clientSocket.close()
    
def main():
    file_name = input("File content name : ")
    Prepare_Chunk(file_name)
    
    while 1:
        Announcer()
        time.sleep(60)

main()