import http.client
import json
import Utiles as Us
PORT = 8080
SERVER = 'localhost'
print(f"\nConnecting to server: {SERVER}:{PORT}\n")
conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/listSpecies?limit=4&json=1")
response = conn.getresponse()

data = response.read().decode("utf-8")
response_dict = json.loads(data)
print("Testing EASY LEVEL-List/species")
print("..................................")
print("The limit chosen --> 4\nThe name of the species:")
for n in Us.print_json_function_1(response_dict):
    print("* " + str(n))
print("__________________________________")
conn.request("GET", "/karyotype?specie=pig&json=1")
response = conn.getresponse()
data = response.read().decode("utf-8")
response_dict = json.loads(data)
print("The specie selected --> Pig")
print("The karyotype is: " + str(Us.print_json_function_3(response_dict)))
print("__________________________________")







