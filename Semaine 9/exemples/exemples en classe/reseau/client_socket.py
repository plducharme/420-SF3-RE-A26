import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("10.18.4.142", 8888))
    client.sendall(b"Ceci est un test")
