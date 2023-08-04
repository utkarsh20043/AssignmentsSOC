import socket
import pickle
import numpy as np

def receive_array(client):
    data = b""
    while True:
        packet = client.recv(1024000000)
        if not packet:
            break
        data += packet
    return pickle.loads(data)

def send_array(client_socket, data):
    serialized_data = pickle.dumps(data)
    client_socket.sendall(serialized_data)
    
def dot_products(q_prime, D_prime, k):
    buff=np.matmul(D_prime,np.transpose(q_prime))
    buff=buff.reshape(-1)
    buff2=np.sort(buff)
    ind_arr=np.zeros(k)
    for i in range(k):
        for j in range(len(D_prime)):
            if(buff2[i]==buff[j]):
                ind_arr[i]=j
                break
    return ind_arr

### CONNECTION BETWEEN CS AND DO STARTS:

HOST = '0.0.0.0'
PORT = 9998

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cloud:
    cloud.bind((HOST,PORT))
    print('waiting for connection with DO....')
    cloud.listen()
    conn, addr = cloud.accept()
    
    with conn:
        D_prime = receive_array(conn)
        print('D_prime: ', D_prime)
    print(f'connection with {addr} i.e. DO closed')
    
### CONNECTION BETWEEN CS AND DO ENDS.

### CONNECTION BETWEEN CS AND QU STARTS.
    
HOST1 = '0.0.0.0'
PORT1 = 9998
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as query:
    query.bind((HOST1,PORT1))
    print('waiting for connection with QU....')
    query.listen()
        
    while True:
        conn, address = query.accept()
        print(f'connected to {address}')
        q_prime = pickle.loads(conn.recv(102400000))
        print('q_prime: ', q_prime)
        k = 10
        L_q = dot_products(q_prime, D_prime, k)
        print('index set sent to QU')
        index_set = pickle.dumps({"L_q": L_q})
        conn.sendall(index_set)
        conn.close()
        print(f'connection with {address} i.e. QU closed')
        
### CONNECTION BETWEEN QU AND CS ENDS.
