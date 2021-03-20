from CLIENT0 import client
from Seq1 import Seq
print("---------EXCERSISE 4----------")
c = Seq()
seq = c.read_fasta("U5.txt")
ip = "localhost"
PORT = 8007
print("Connection to server with ip: ", ip, "Port: ", PORT)
c = client(ip, PORT)
print("To server: Sending the U5.txt sequence ")
print(c.talk("Sending the U5.txt sequence"))
print("To server: ", seq)
print(c.talk(seq))
