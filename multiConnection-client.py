import socket
import sys

SERVER_HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, PORT))
message = input("Type your message (Type 'exit' to close): ")
client.sendall(bytes(message, 'UTF-8'))
if message == "exit":
	client.close()
	sys.exit()

while True: 
	in_data = client.recv(2048)
	print("From Server:", in_data.decode())
	print("---------------------------------------------------------")
	out_data = input("Type your new message (Type 'exit' to close): ")
	client.sendall(bytes(out_data,'UTF-8'))
	if out_data == "exit":
		break

client.close()