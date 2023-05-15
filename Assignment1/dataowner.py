import socket
import random
import json

HOST = "127.0.0.1" # Standard loopback interface address (localhost)
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as owner:
    owner.bind((HOST,PORT))
    print('waiting for connection....')
    owner.listen()

    while True:
        conn, address = owner.accept()
        print(f'connected to {address}')
        query = json.loads(conn.recv(1024).decode())
        i = int(query["query"])
        print(f'message from client is: {i}')
        num = random.randint(1,10001)
        print('random number generated is: {}'.format(num))
        num1 = num*i
        data = json.dumps(num1).encode()
        conn.sendall(data)
        conn.close()
        print(f'connection with {address} closed')
