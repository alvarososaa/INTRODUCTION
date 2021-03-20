from CLIENT0 import client
from Seq1 import Seq
print("---------EXCERSISE 5----------")
s = Seq()
seq = s.read_fasta("FRAT1.txt")
ip = "localhost"
PORT = 8008
print("Connection to server with ip: ", ip, "Port: ", PORT)
c = client(ip, PORT)
print("Gene FRAT1: ", seq)
c.talk("Sending the FRAT1 sequence , in 5 fragments of 10 basis")
for i in range(0, 5):
    print(f"Fragment {i + 1}: {seq[i * 10: (i * 10) + 10]}")
    c.talk(f"Fragment {i + 1}: {seq[i * 10: (i * 10) + 10]}")