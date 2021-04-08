import socket
import termcolor
from CLIENT0 import client
import server_utils
from Seq1 import Seq
list_sequences = ["ACACACACACACACA" , "ATATATATATAT" , "AGAGCGAGCGAGT" , "ATATATCTGT" , "AAAA"]
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
PORT = 8080
IP = "localhost"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()
        exit()

    print("A client has connected to the server!")
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    answer = msg.split(" ")
    if len(answer) == 1:
        command = answer[0]
    else:
        command = answer[0]
        extra = answer[1]
    if command == "PING":
        termcolor.cprint(command , "green")
        server_utils.ping()
        response = "OK\n"
    elif command == "GET":
        termcolor.cprint(command, "green")
        try:
            if 0 <= int(extra) <= 4:
                response = list_sequences[int(extra)]
            else:
                response = "NOT COMMAND FOUND"
        except ValueError:
            response = "NOT COMMAND FOUND"
    elif command == "INFO":
        termcolor.cprint(command, "green")
        seq = Seq(extra)
        response = server_utils.sequence(seq)
        print(response)
    elif command == "COMP":
        termcolor.cprint(command, "green")
        complement = Seq(extra)
        response = f"{complement.complement()}\n"
        print(response)
    elif command == "REV":
        termcolor.cprint(command, "green")
        reverse = Seq(extra)
        response = f"{reverse.reversed()}\n"
        print(response)
    elif command == "GENE":
        termcolor.cprint(command, "green")
        if extra == "U5" or extra == "ADA" or extra == "FRAT1" or extra == "FXN" or extra == "RNU6_269P":
            FOLDER = "./SEQUENCES/"
            gene = Seq()
            response = gene.read_fasta(FOLDER + extra + ".txt")
            print(response)
        else:
            response = "NO GENE FOUND"
            print(response)


    else:
        response = "NOT COMMAND FOUND\n"
    cs.send(str(response).encode())
    cs.close()