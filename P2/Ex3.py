from CLIENT0 import client
import socket
print("---------EXCERSISE 2----------")
ip = "localhost"
PORT = 8001
c = client(ip, PORT)
c.talk()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, PORT))
s.send(str.encode("Hello from the client"))
msg = s.recv(2048)
print(msg)
s.close()
