from sage.all import *

class RSA:

    def __init__(self, k, e=65537): 
        self.k = k
        self.e = e
        self.generate_keys()

    def generate_keys(self):
    #Step 1:
        while True:
            p = random_prime(2 ** self.k - 1, lbound=2 ** (self.k - 1))
            q = random_prime(2 ** self.k - 1, lbound=2 ** (self.k - 1))
            if p != q:
                break
    #Step 2 & 3:
        self.p = p
        self.q = q
        self.N = p * q
        self.phi_N = (p - 1) * (q - 1)
    #Step 4:
        self.d = pow(self.e, -1, self.phi_N)

    def get_public_key(self):

        #we know that the public key is the pair (e, N)
        return self.e, self.N
    
    def encrypt(self, plaintext):
        if plaintext >= self.N:
            return "Invalid size of plaintext!"
        
        #we know that the encrpted message m' = rem((m)^e, N) which is also called as ciphertext.
        return pow(plaintext, self.e, self.N)

    def decrypt(self, ciphertext):
        if int(ciphertext) >= self.N:
            return "Invalid size of ciphertext!"

        #we know that the decrypted message m = rem((m')^d, N) which is also called as plaintext.
        return pow(ciphertext, self.d, self.N)
    
    def bytes_to_int(self, object):   #function for bytes to integer conversion
        hex_str = object.hex()
        return int(hex_str, 16) #convert hexadecimal string to integer

    def int_to_bytes(self, integer):   #function for integer to byted conversion
        hex_str = hex(integer)[2:]  
        if len(hex_str) % 2 != 0:
            hex_str = '0' + hex_str  
        return bytes.fromhex(hex_str) #convert intger to hexadecimal string

    
A = input("enter the value of k: ")
k = int(A)

#creating an rsa instance.
rsa = RSA(k)
public_key = rsa.get_public_key()
plaintext = "hello!"

#conversion_to_bytes
m = plaintext.encode()

#conversion_to_integer
integer = rsa.bytes_to_int(m)
ciphertext = rsa.encrypt(integer)

#we have the message m with us. And we have it encrypted i.e. we have m'.
#next we have to decrypt it.
decrypted_m = rsa.decrypt(ciphertext)

#conversion_to_bytes.
byte = rsa.int_to_bytes(decrypted_m)

#conversion_to_text.
message = byte.decode()

#final output required to be printed.
print("Public Key:", public_key)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", message)
