import socket
from cryptography.fernet import Fernet

# load key
with open("secret.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

command = "MOVE_FORWARD".encode()

encrypted_command = cipher.encrypt(command)

client = socket.socket()

client.connect(("localhost", 9999))

client.send(encrypted_command)

response = client.recv(1024)

decrypted_response = cipher.decrypt(response)

print("Robot response:", decrypted_response.decode())

client.close()
