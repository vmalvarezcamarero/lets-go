import http.client
import json

GENE_DICT = {"FRAT1":"ENSG00000165879",
     "ADA":"ENSG00000196839",
     "FXN":"ENSG00000165060",
     "RNU6_269P":"ENSG00000212379",
     "MIR633":"ENSG00000207552",
     "TTTY4C":"ENSG00000226906",
     "RBMY2YP":"ENSG00000227633",
     "FGFR3":"ENSG00000068078",
     "KDR":"ENSMUSG00000062960",
     "ANK2":"ENSG00000145362"
}
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = GENE_DICT["MIR633"]
PARAMETERS = "?content-type=application/json"
connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + ID + PARAMETERS)
response = connection.getresponse()
print("Response received!:", response.status, response.reason)
if response.status == 200:
    response = json.loads(connection.getresponse().read().decode())
    print(json.dumps(response, indent=4, sort_keys=True))
    print ("Gene:", ID)
    print("Description:", response["desc"])
    print("Bases:", response["seq"])
elif response.status == 404:
    print("Check if the ENDPOINT is made correctly")