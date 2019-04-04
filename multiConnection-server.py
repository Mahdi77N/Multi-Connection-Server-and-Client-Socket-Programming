import socket
import threading

class clientThread(threading.Thread):
	def __init__(self, clientAddress, clientsocket):
		threading.Thread.__init__(self)
		self.socket = clientsocket
		print ("New connection added:", clientAddress)

	def run(self):
		print("Connection from:", clientAddress)
		message = ''
		while True:
			data = self.socket.recv(2048)
			message = data.decode()
			if message == "exit":
				break
			print("From client:", message)
			self.socket.send(bytes(message, 'UTF-8'))
		print ("Client at", clientAddress, "disconnected :( with message: 'exit'")


LOCALHOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started :)")
print("Waiting for client request...")

while True:
	server.listen(1)
	clientsock, clientAddress = server.accept()
	newthread = clientThread(clientAddress, clientsock)
	newthread.start()