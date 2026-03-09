import socket

server = socket.socket()

server.bind(("localhost", 9999))
server.listen(1)

print("Robot waiting for command...")

conn, addr = server.accept()
print("Connected from:", addr)

data = conn.recv(1024).decode()  # 1024 bytes
print("Command received:", data)

conn.send("ACK".encode())
conn.close()
