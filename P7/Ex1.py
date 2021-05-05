import http.client
import json
SERVER = "rest.ensembl.org"
print("SERVER: ", SERVER)
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
print("URL:" , ENDPOINT + PARAMS)
connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
answer_decoded = response.read().decode()
dict_decode = json.loads(answer_decoded) #By this, we get the answer that they are being asked for
if dict_decode["ping"] == 1:
    print("PING IS OK!!! The database is running")
else:
    print("PRINT IS NOT OK")
