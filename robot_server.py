import socket
from cryptography.fernet import Fernet

# load shared secret key
with open("secret.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

server = socket.socket()

server.bind(("localhost", 9999))
server.listen(1)

print("Robot waiting for command...")

conn, addr = server.accept()
print("Connected from:", addr)

encrypted_data = conn.recv(1024)

# decrypt command
decrypted_data = cipher.decrypt(encrypted_data)

data = decrypted_data.decode()

print("Decrypted command received:", data)

response = cipher.encrypt(b"ACK")
conn.send(response)

if data == "MOVE_FORWARD":
    print("Robot moving forward")

elif data == "STOP":
    print("Robot stopping")

conn.close()
