import socket

host = '127.0.0.1'  # localhost
port = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Server listening on {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print(f"Received from client: {data.decode()}")

conn.sendall(b"Hello from server!")
conn.close()

