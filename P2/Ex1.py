from CLIENT0 import client
print("---------EXCERSISE 1----------")
ip = "localhost"
PORT = 8008
c = client(ip, PORT)
c.ping()
print(f"IP: {c.ip} ,  {c.port}")