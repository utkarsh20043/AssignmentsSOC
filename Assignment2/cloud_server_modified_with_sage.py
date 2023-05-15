import socket
import json
from sage.all import *

HOST1 = "127.0.0.1" # Standard loopback interface address (localhost)
PORT1 = 9998

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cloud:
    cloud.bind((HOST1,PORT1))
    print('waiting for connection....')

    cloud.listen()

    while True:
        conn, address = cloud.accept()
        print(f'connected to {address}')
        data = json.loads(conn.recv(1024).decode())
        print(f'message from client is: {data}')
        d = int(data["data"])
        
        #factorisation performed with storing each factor in the list.
        factors = [factor[0] for factor in factor(d)]

        result = json.dumps({"result": factors}).encode()
        conn.sendall(result)
        conn.close()
        print(f'connection with {address} closed')