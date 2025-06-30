# 🖧 Networking Projects

This folder contains basic Python socket programming examples for learning how clients and servers communicate over the network.

## 🔧 Projects

### 1. `socket_client.py`
- Connects to an external server (`example.com`) using a raw TCP socket.
- Sends a basic HTTP GET request and prints the response.

### 2. `socket_server.py`
- A local TCP server that listens for a client on `localhost:65432`.
- Accepts one message from the client and responds with a confirmation.

### 3. `socket_chat_client.py`
- Connects to the local socket server.
- Sends a message typed by the user and prints the server's response.

## 🛠️ How to Run

### Start the server first:

```bash
python socket_server.py
