import socket
from termcolor import colored
class client:
    def __init__(self , ip, port):
        self.ip = ip
        self.port = port
    def ping(self):
        print("OK")
    def __str__(self):
        return f"Connection to server {self.ip} PORT: {self.port}"
    def talk(self , msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        answer = s.recv(1024).decode("utf-8")
        s.close()
        return  answer
    def debug_talk(self, msg):
        x = colored(client.talk(self, msg), "yellow")
        return x





