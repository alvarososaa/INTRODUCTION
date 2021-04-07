import socket
from CLIENT0 import client
import server_utils
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
    print(len(answer))
    if len(answer) == 1:
        command = answer[0]
    else:
        command = answer[0]
        number = answer[1]
    if command == "PING":
        server_utils.ping()
        response = "OK\n"
    elif command == "GET":
        response = f"{list_sequences[int(number)]}\n"

    else:
        response = "NOT COMMAND FOUND\n"
    cs.send(str(response).encode())
    cs.close()