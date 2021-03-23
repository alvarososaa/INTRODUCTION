from CLIENT0 import client
from Seq1 import Seq
import termcolor
print("---------EXCERSISE 4----------")
c = Seq()
seq = c.read_fasta("U5.txt")
ip = "localhost"
PORT = 8008
print("Connection to server with ip: ", ip, "Port: ", PORT)
c = client(ip, PORT)
termcolor.cprint("To server: Sending the U5.txt sequence", "blue")
print(c.debug_talk("Sending the U5.txt sequence"))
termcolor.cprint(f"To server: {seq} ", "blue")
print(c.debug_talk(seq))