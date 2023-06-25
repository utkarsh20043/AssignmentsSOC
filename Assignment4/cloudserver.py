import socket
import json

HOST1 = '0.0.0.0'  
# 0.0.0.0 is a non-routable meta-address that also specifies all IP # addresses on all interfaces on the system
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
        factors = []
        i = 1
        
        while(i <= d):
            c = 0
            if(d % i == 0):
                j = 1
                while(j <= i):
                    if(i % j == 0):
                        c = c + 1
                    j = j + 1
                    
                if (c == 2):
                    factors.append(i)
            i = i + 1
     
        result = json.dumps({"result": factors}).encode()
        conn.sendall(result)
        conn.close()
        print(f'connection with {address} closed')