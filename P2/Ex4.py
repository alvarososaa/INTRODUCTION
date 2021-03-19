from CLIENT0 import client
from pathlib import Path
print("---------EXCERSISE 4----------")
sequence = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P0/SEQUENCES/U5.txt"
ip = "localhost"
PORT = 8006
print("Connection to server with ip: ", ip, "Port: ", PORT)
c = client(ip, PORT)
print("To server: Sending the U5.txt sequence ")
print(c.talk("Sending the U5.txt sequence"))
print("To server: ", Path(sequence).read_text())
print(c.talk(Path(sequence).read_text()))
