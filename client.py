import socket
import random
from utils import xor_encrypt, xor_decrypt

HOST = '127.0.0.1'
PORT = 5001

p = 23
g = 5

client_secret = random.randint(1, 100)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    A = pow(g, client_secret, p)
    s.send(str(A).encode())

    B = int(s.recv(1024).decode())
    K = pow(B, client_secret, p)

    message = "Hello server"
    s.send(xor_encrypt(message, K))

    response = xor_decrypt(s.recv(1024), K)
    print(f"[CLIENT] Response: {response}")
