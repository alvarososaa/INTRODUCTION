import socket
import termcolor
connection = 0
ip = "localhost"
PORT = 8010
s = socket.socket()
s.bind((ip, PORT))
s.listen(45)
connection = 0
while True:
    connection += 1
    print("Connection", connection , "from the ip: ", ip, "PORT: ", PORT)
    print(f"Waiting for connections at... {ip} PORT: {PORT}")
    conex , adresse = s.accept()
    conex.send(str.encode("Hello from the teachers server"))
    msg = conex.recv(2048).decode("utf-8")
    termcolor.cprint(f"RESPONSE FROM THE CLIENT SERVER: {msg}", "red")
    conex.close()