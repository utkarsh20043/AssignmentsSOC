import socket
import pickle
import numpy as np
from sage.all import *
from numpy import random
import json
import random
from decimal import Decimal

def receive_array(client):
    data = b""
    while True:
        packet = client.recv(1024000000)
        if not packet:
            break
        data += packet
        if len(packet) < 4096:
            break
    return pickle.loads(data)

def send_array(client_socket, data):
    serialized_data = pickle.dumps(data)
    client_socket.sendall(serialized_data)

def perturb_pi(a,b,c,d1,ax,n,pi):
    D_prime=np.concatenate((a,b,c,d1),axis=ax)
    D_prime=np.transpose(D_prime)
    D_prime2 = np.array(D_prime)
    for i in range(n):
        D_prime[pi[i]]=D_prime2[i]
    D_prime=np.transpose(D_prime)
    return D_prime

def read_database_txt(filename):
    points_list = []
    with open(filename, 'r') as f:
        for line in f:
            point_str = line.strip().split(": ")[1]
            point_str = point_str.strip("[]")  
            point = np.array([float(x) for x in point_str.split()])
            points_list.append(point)
    return np.array(points_list)

def encrypt(n,g,m):
    r=random.randint(1,n-1)
    cipher1=pow(g,int(m),int(n)**2)
    cipher2=pow(r,int(n),int(n)**2)
    cipher=cipher1*cipher2
    return cipher
            
def pi_inverse(B, i):
    e = len(B)
    for j in range(e):
        if B[j] == i:
            return j 
                
### CONNECTION BETWEEN DO AND CS STARTS :
  
HOST = "127.0.0.1"
PORT = 9998

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cloud:
    cloud.connect((HOST,PORT))
    d=50
    n1=10000
    
    if __name__ == "__main__":
        filename = "database.txt"
        D = read_database_txt(filename)
        print('D :', D)
        
    c=random.randint(1,5)

    epsilon=random.randint(1,5)
    
    S=np.random.randint(3,size=d+1)

    tou=np.random.randint(5,size=c)

    V=np.random.randint(10,size=(n1,epsilon))

    pmag=(np.sum(np.square(D),axis=1)).reshape(n1,1)

    D_prime_1=S[0:d]-2*D
    D_prime_2=S[d]+pmag

    tou=np.multiply(np.ones((n1,c)),tou)

    pi=np.arange(d+c+1+epsilon)
    np.random.shuffle(pi)

    D_dot=perturb_pi(D_prime_1,D_prime_2,tou,V,1,d+c+1+epsilon,pi)

    eta = d+c+1+epsilon
    
    while True:
        M = np.random.uniform(0,5,size=(eta, eta))
        if np.linalg.det(M) != 0:
            break
    M_inv = np.linalg.inv(M)

    D_prime = np.dot(D_dot, M_inv)
    
    send_array(cloud,D_prime)
    cloud.close()

### CONNECTION BETWEEN DO AND CS ENDS.

### CONNECTION BETWEEN QU AND DO STARTS :

HOST1 = "127.0.0.1"
PORT1 = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as owner:
    owner.bind((HOST1,PORT1))
    print('waiting for connection with QU...')
    owner.listen()
    
    while True:
        conn, address = owner.accept()
        print(f'connected to {address}')
        received_data = json.loads(conn.recv(102400000).decode())
        pubk = received_data['pubk']
        Eq = received_data['Eq']
        print('pubk : ', pubk)
        print('Eq : ', Eq)
        
        eta = d + c + epsilon + 1

        beta_q = Decimal(random.randint(1,10))
        
        R = np.random.randint(low=0, high=10, size=c)

        allow_query = input("Do you want to allow query? (y/n): ")

        if allow_query.lower() == "y":
            print("Query is allowed.")
            A=np.zeros(eta)
            for i in range(eta):
                A[i]=encrypt(pubk[0], pubk[1], 0)
                for j in range(eta):
                    t = pi_inverse(pi,j)
                    if t < d:
                        phi = int(beta_q * int(M[i, j]))
                        A[i]= A[i]*pow(Eq[t],phi,int(pubk[0]**2))
                    elif t == d:
                        phi = int(beta_q * int(M[i, j]))
                        A[i] = A[i]*encrypt(int(pubk[0]),int(pubk[1]),phi)
                    elif t <= d + c:
                        omega = t - d - 1
                        phi = int(beta_q * int(M[i, j]) * int(R[omega]))
                        A[i] = A[i]*encrypt(int(pubk[0]),int(pubk[1]),phi)
                        
            A_q = pickle.dumps({"A_q": A})
            conn.sendall(A_q)
            
        elif allow_query.lower() == "n":
            n = 0
            n_1 = pickle.dumps(n)
            conn.sendall(n_1)
            print("Query disallowed.")
            
        conn.close()
        print(f'connection with {address} i.e. QU closed')
            
### CONNECTION BETWEEN QU AND DO ENDS.