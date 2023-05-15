import socket
import json

HOST = "127.0.0.1"
PORT = 9999

HOST1 = "127.0.0.1"
PORT1 = 9998

#query sent to cloud and data received.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as owner:
    owner.connect((HOST, PORT))
    n = input("enter positive integer: ")
    query = {"query": n}
    owner.sendall(json.dumps(query).encode())
    data = {"data":owner.recv(1024).decode()}

#data sent to cloud and result received.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cloud:
    cloud.connect((HOST1,PORT1))
    cloud.sendall(json.dumps(data).encode())
    result = json.loads(cloud.recv(1024).decode())
    print('prime factorisation: ')
    print(result["result"])
