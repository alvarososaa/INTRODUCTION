from CLIENT0 import client
from Seq1 import Seq
print("---------EXCERSISE 5----------")
s = Seq()
seq = s.read_fasta("FRAT1.txt")
ip = "localhost"
PORT = 8008
PORT_1 = 8009
print("Connection to server with ip: ", ip, "Port: ", PORT)
print("Connection to server with ip: ", ip, "Port: ", PORT_1)
c = client(ip, PORT)
t = client(ip , PORT_1)
print("Gene FRAT1: ", seq)
c.talk("Sending the FRAT1 sequence , in  fragments of 10 basis")
t.talk("Sending the FRAT1 sequence , in  fragments of 10 basis")
for i in range(0, 10):
    if i % 2:
        print(f"Fragment {i + 1}: {seq[i * 10: (i * 10) + 10]}")
        c.talk(f"Fragment {i + 1}: {seq[i * 10: (i * 10) + 10]}")
    else:
        print(f"Fragment {i + 1}: {seq[i * 10: (i * 10) + 10]}")
        t.talk(f"Fragment {i + 1}: {seq[i * 10: (i * 10) + 10]}")
