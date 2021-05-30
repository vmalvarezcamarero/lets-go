import http.server
import json
import utiles as us

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
PARAMETERS = "?content-type=application/json"
connection = http.client.HTTPConnection(SERVER)


def function_1(arguments):
    ENDPOINT = "/info/species"
    connection.request("GET", ENDPOINT + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    count = len(response_dict["species"])
    empty_list = []
    for n in range(0, int(arguments["limit"][0])):
        empty_list.append(response_dict["species"][n]["common_name"])

    context = {"number_seq": count,
               "limit": arguments["limit"][0],
               "names": empty_list}
    return context

def function_2(arguments):
    ENDPOINT = "/info/species"
    connection.request("GET", ENDPOINT + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    count = len(response_dict["species"])
    empty_list = []
    for n in range(0, 310):
        empty_list.append(response_dict["species"][n]["common_name"])

    context = {"number_seq": count,
               "limit": arguments["limit"][0],
               "names": empty_list}
    return context

def function_3(arguments):
    ENDPOINT = "/info/assembly/"
    specie = arguments["specie"][0].replace(" ", "_")
    connection.request("GET", ENDPOINT + specie + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    empty_list = []
    for n in response_dict["karyotype"]:
        empty_list.append(n)

    context = {"kar": empty_list}
    return context

def function_4(arguments):
    ENDPOINT = "/info/assembly/"
    specie = arguments["specie"][0].replace("+", "_")
    connection.request("GET", ENDPOINT + specie + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    for n in range(0, len(response_dict['top_level_region'])):
        if response_dict['top_level_region'][n]["name"] == arguments["chromosome"][0]:
            length = response_dict['top_level_region'][n]["length"]
            context = {"length": length}
            return context
        else:
            pass


def function_5(arguments):
    ENDPOINT = "/sequence/id/"
    user_gene = arguments["gene"][0]
    ID = GENE_DICT[user_gene]
    connection.request("GET", ENDPOINT + ID + PARAMETERS)

    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())

    context = {"seq_name": user_gene,
               "seq": response_dict["seq"]}
    return context

def function_6(arguments):
    ENDPOINT = "/sequence/id/"
    user_gene = arguments["gene"][0]
    ID = GENE_DICT[user_gene]
    connection.request("GET", ENDPOINT + ID + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    l = str(int(response_dict["desc"].split(":")[4]) - int(response_dict["desc"].split(":")[3]) + 1)

    context = {"seq_name": user_gene,
               "id": ID,
               "length": l,
               "start": response_dict["desc"].split(":")[3],
               "end": response_dict["desc"].split(":")[4],
               "name": response_dict["desc"].split(":")[1]
               }
    return context

def function_7(arguments):
    ENDPOINT = "/sequence/id/"
    user_gene = arguments["gene"][0]
    ID = GENE_DICT[user_gene]
    connection.request("GET", ENDPOINT + ID + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    seq = response_dict["seq"]
    seq1 = us.Seq(seq)
    inf_dict = seq1.count_bases_6()[0]
    inf_dict_perc = seq1.count_bases_6()[1]

    context = {"seq_name": user_gene,
               "count": inf_dict,
               "percentage": inf_dict_perc,
               }
    return context


def json_function_1():
    ENDPOINT = "/info/species"
    connection.request("GET", ENDPOINT + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    return response_dict

def print_json_function_1(response_dict):
    empty_list = []
    for n in range(0, 4):
        empty_list.append(response_dict["species"][n]["common_name"])

    return empty_list

def print_json_function_2():
    ENDPOINT = "/info/assembly/"
    specie = "pig"
    connection.request("GET", ENDPOINT + specie + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    return response_dict

def print_json_function_3(response_dict):
    empty_list = []
    for n in response_dict["karyotype"]:
        empty_list.append(n)
    return empty_list