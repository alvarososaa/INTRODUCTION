from CLIENT0 import client
print("---------EXCERSISE 2----------")
ip = "localhost"
PORT = 8004
c = client(ip, PORT)
x = c.talk()
print(x)


