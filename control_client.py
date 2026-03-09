import socket

client = socket.socket()

client.connect(("localhost", 9999))

command = "MOVE_FORWARD"

client.send(command.encode())

response = client.recv(1024).decode()

print("Robot response:", response)

client.close()
