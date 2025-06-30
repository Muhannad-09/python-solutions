import socket

host = "example.com"
port = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
client_socket.send(request.encode())

response = client_socket.recv(4096)
print("Response from server:")
print(response.decode(errors="ignore"))

client_socket.close()
