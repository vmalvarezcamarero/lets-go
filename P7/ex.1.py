import http.client
import json
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
answer_decoded = response.read().decode()
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)
if dict_response["ping"] == 1:
    print("PING OK! The data base is running")
else:
    print("Database is down!!!")