import http.client
import json
import termcolor
PORT = 8080
SERVER = 'localhost'
print(f"\nConnecting to server: {SERVER}:{PORT}\n")
conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", "/info/species")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
# -- Read the response message from the server
r1 = conn.getresponse()
# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")
# -- Read the response's body
data1 = r1.read().decode("utf-8")
# -- Create a variable with the data,
# -- form the JSON received
people = json.loads(data1)
print("CONTENT: ")
print(people)