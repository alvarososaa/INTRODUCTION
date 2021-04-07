import socket
n = input("Please enter what do you want send to the server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8080))
s.send(str.encode(n))
msg = s.recv(2048)
print(msg)
s.close()
