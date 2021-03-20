from CLIENT0 import client
print("---------EXCERSISE 3----------")
ip = "localhost"
PORT = 8008
print("Connection to server with ip: ", ip, "Port: ", PORT)
c = client(ip, PORT)
x = c.talk("TESTING!")
print("RESPONSE: ")
print(x)


