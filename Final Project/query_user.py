import socket
import json
import pickle
import numpy as np
from sage.all import *
import random

### CONNECTION BETWEEN QU AND DO STARTS:

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as owner:
    owner.connect((HOST,PORT))

    class paillier_class:
        def __init__(self):
            c=1
            while c==1:
                p1=random_prime(2**5,True,2**4)
                p2=random_prime(2**5,True,2**4)
                if p1!=p2 and gcd(p1*p2,(p1-1)*(p2-1)==1):
                    break
            n=int(p1*p2)
            self.n=n
            self.lam=int(lcm(p1-1,p2-1))
            a=0
            self.a=a
            while True :
                g=int(random.randint(1,n**2-1))
                self.g=g
                L=pow(g,self.lam,n**2)
                self.a=(int(L)-1)//self.n
                if gcd(self.a,n)==1 and gcd(self.g,n)==1 :
                    break
            self.u=int(inverse_mod(self.a,n))
            
        def get_public_key(self):
            self.pubk=(self.n,self.g)
            return self.pubk
        
        def encrypt(self,m):
                r=random.randint(1,self.n-1)
                cipher1=pow(self.g,m,self.n**2)
                cipher2=pow(r,self.n,self.n**2)
                cipher=cipher1*cipher2
                return cipher
            
        def decrypt(self,cipher):
            t=pow(int(cipher),self.lam,self.n**2)
            k=(int(t)-1)//int(self.n)
            m=mod(k*self.u,self.n)
            return m
        
    d=50
    o=paillier_class()
    pubk=o.get_public_key()

    q=np.random.randint(low=-10,high=10,size=(d))

    Eq = []
    for i in range(d):
        m = int(q[i])
        cipher = o.encrypt(m)
        Eq.append(cipher)
        
    data = {"pubk": pubk, "Eq": Eq}
    owner.sendall(json.dumps(data).encode())

    result1 = pickle.loads(owner.recv(1024000000))
        
    if (result1 == 0):
        print("query disallowed by DO.")
        exit(1)
            
    Aq = result1['A_q']
    print('A_q: ', Aq)
    L = len(Aq)
            
### CONNECTION BETWEEN QU AND DO ENDS.

### CONNECTION BETWEEN QU AND CS STARTS.

q_prime = np.zeros(L)
for i in range(L):
    m=Aq[i]
    ptxt=o.decrypt(m)
    if(ptxt>1000):
        ptxt=int(ptxt)
        ptxt-=pubk[0]
    q_prime[i]=ptxt

HOST1 = "127.0.0.1"
PORT1 = 9998

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as query:
    query.connect((HOST1,PORT1))    
    query.sendall(pickle.dumps(q_prime))
    result2 = pickle.loads(query.recv(10240000))
    index_set = result2['L_q']
    print('index set:', index_set)
                
### CONNECTION BETWEEN QU AND CS ENDS.