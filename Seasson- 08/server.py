import socket
connection = 0
ip = "localhost"
PORT = 8004
s = socket.socket()
s.bind((ip, PORT))
s.listen(45)
connection = 0
while True:
    n = input("What message do you want to send to the client: ")
    connection += 1
    print("Connection", connection)
    print(f"Waiting for connections at... {ip} PORT: {PORT}")
    conex , adresse = s.accept()
    conex.send(str.encode(n))
    msg = conex.recv(2048).decode("utf-8")
    print(msg)
    conex.close()