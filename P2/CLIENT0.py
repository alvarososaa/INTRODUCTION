import socket
class client:
    def __init__(self , ip, port):
        self.ip = ip
        self.port = port
    def ping(self):
        print("OK")
    def __str__(self):
        return f"Connection to server {self.ip} PORT: {self.port}"
    def talk(self):
        print("Conexion completing...")
        s = socket.socket()
        s.bind((self.ip, self.port))
        while True:
            conexion , adresse = s.accept()
            conexion.send(str.encode("Hello from the server"))
            conexion.close()
