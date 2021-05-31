import http.client
import json
import Utiles as Us
PORT = 8080
SERVER = 'localhost'
print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
try:

    conn.request("GET", "/listSpecies?limit=4&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_1(response_dict)

    conn.request("GET", "/listSpecies?limit=aaaa&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_1(response_dict)

    conn.request("GET", "/karyotype?specie=pig&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_2(response_dict)

    conn.request("GET", "/karyotype?specie=box3&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_2(response_dict)

    conn.request("GET", "/chromosomeLength?specie=pig&chromosome=4&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_3(response_dict)

    conn.request("GET", "/chromosomeLength?specie=box3&chromosome=aaa&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_3(response_dict)

    conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_4(response_dict)

    conn.request("GET", "/geneSeq?gene=box3&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_4(response_dict)


    conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_5(response_dict)

    conn.request("GET", "/geneInfo?gene=box3&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_5(response_dict)

    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_6(response_dict)

    conn.request("GET", "/geneCalc?gene=box3&json=1")
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    response_dict = json.loads(data)
    Us.print_json_function_6(response_dict)


except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()







