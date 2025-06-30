import socket

host = '127.0.0.1'  # localhost
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
