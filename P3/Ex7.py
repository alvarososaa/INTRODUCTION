from CLIENT0 import client
import termcolor
FOLDER = "./SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
ip = "localhost"
PORT = 8080
s = client(ip, PORT)
termcolor.cprint("TESTING THE PING", "green")
print(s.talk("PING"))
termcolor.cprint("TESTING GET", "green")
print("GET 0: ", s.talk("GET 0"))
print("GET 1: ", s.talk("GET 1"))
print("GET 2: ", s.talk("GET 2"))
print("GET 3: ", s.talk("GET 3"))
print("GET 4: ", s.talk("GET 4"))
termcolor.cprint("TESTING INFO", "green")
sequence = s.talk("GET 0")
print("INFO: ", s.talk("INFO " + sequence))
termcolor.cprint("TESTING COMPLEMENT", "green")
print("COMPLEMENT: ", s.talk("COMP " + sequence))
termcolor.cprint("TESTING REVERSED", "green")
print("REVERSED: ", s.talk("REV " + sequence))
termcolor.cprint("TESTING GENE", "green")
for element in range(0, len(gene_list)):
    print(gene_list[element],  ":", s.talk("GENE " + gene_list[element]) , "\n")





