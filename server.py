import socket
import random
from utils import xor_decrypt, xor_encrypt

HOST = '127.0.0.1'
PORT = 5001

p = 23
g = 5

server_secret = random.randint(1, 100)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("[SERVER] Waiting...")
    conn, addr = s.accept()

    with conn:
        A = int(conn.recv(1024).decode())
        B = pow(g, server_secret, p)
        conn.send(str(B).encode())

        K = pow(A, server_secret, p)

        encrypted = conn.recv(1024)
        message = xor_decrypt(encrypted, K)

        print(f"[SERVER] Received: {message}")

        response = "OK"
        conn.send(xor_encrypt(response, K))