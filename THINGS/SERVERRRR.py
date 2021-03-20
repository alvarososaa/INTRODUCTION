import socket
n = input("Please enter the message you want to send to the client")
s = socket.socket()
s.bind(("localhost", 8001))
s.listen(45)
while True:
    conexion, adresse = s.accept()
    print(adresse)
    print("Conexion completing...")
    conexion.send(str.encode(n))
    conexion.close()