
import json
import utiles as us
import http.client

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
connection = http.client.HTTPConnection(SERVER)
PARAMETERS = "?content-type=application/json"


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
    connection.close()
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
    connection.close()
    return context

def function_3(arguments):
    specie = arguments["specie"][0].replace(" ", "_")
    ENDPOINT = "/info/assembly/" + specie
    connection.request("GET", ENDPOINT + PARAMETERS)
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    context = {"kar": response_dict["karyotype"]}
    connection.close()
    return context

def function_4(arguments):
    specie = arguments["specie"][0].replace(" ", "_")
    ENDPOINT = "/info/assembly/" + specie
    connection.request("GET", ENDPOINT + PARAMETERS)
    chromosome = arguments["chromosome"][0]
    context = {}
    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())
    for n in range(0, len(response_dict['top_level_region'])):
        if chromosome in response_dict["top_level_region"][n]["name"]:
            length = response_dict['top_level_region'][n]["length"]
            context = {"length": length}

        else:
            pass

    connection.close()

    return context

def function_5(arguments):
    ENDPOINT = "/sequence/id/"
    user_gene = arguments["gene"][0]
    ID = GENE_DICT[user_gene]
    connection.request("GET", ENDPOINT + ID + PARAMETERS)

    response = connection.getresponse()
    response_dict = json.loads(response.read().decode())

    context = {"seq_name": user_gene,
               "seq": response_dict["seq"]}
    connection.close()
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
               "name": response_dict["desc"].split(":")[2]
               }
    connection.close()
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
    connection.close()
    return context

def error():
    context = {}
    return context


def print_json_function_1(response_dict):
    print("\n__________________________________")
    print("Testing EASY LEVEL-List/species")
    print("__________________________________")
    try:
        print("The limit chosen --> "+ response_dict["limit"] + "\nThe name of the species:")
        for n in range(0, len(response_dict["names"])):
            print("* " + response_dict["names"][n])

    except KeyError:
        print("THE DATA INTRODUCED IS WRONG!!\n")



def print_json_function_2(response_dict):
    print("\n__________________________________")
    print("Testing EASY LEVEL-Karyotype")
    print("__________________________________")

    try:
        a = response_dict["kar"]
        print("The specie selected --> Pig")
        print("The karyotype is: ")
        for n in range(0, len(response_dict["kar"])):
            print(" - " + response_dict["kar"][n])

    except KeyError:
        print("THE DATA INTRODUCED IS WRONG!!\n")


def print_json_function_3(response_dict):
    print("\n__________________________________")
    print("Testing EASY LEVEL-ChromosomeLength")
    print("__________________________________")

    try:
        a = response_dict["length"]
        print("The specie selected --> Pig")
        print("The chromosome selected --> 4")
        print("The length is: " + str(response_dict["length"]))
        print("\n\n")
    except KeyError:
        print("THE DATA INTRODUCED IS WRONG!!\n")

def print_json_function_4(response_dict):
    print("\n++++++++++++++++++++++++++++++++++")
    print("Testing MEDIUM LEVEL-GeneSequence")
    print("++++++++++++++++++++++++++++++++++")
    try:
        a = response_dict["seq"]
        print("The GENE selected --> " + response_dict["seq_name"])
        print("The complete sequence: " + response_dict["seq"])
    except KeyError:
        print("THE DATA INTRODUCED IS WRONG!!\n")

def print_json_function_5(response_dict):
    print("\n++++++++++++++++++++++++++++++++++")
    print("Testing MEDIUM LEVEL-InfoSequence")
    print("++++++++++++++++++++++++++++++++++")
    try:
        print("The GENE selected --> " + response_dict["seq_name"])
        print("The length of the sequence -->" + response_dict["length"])
        print("START --> " + response_dict["start"])
        print("END --> " + response_dict["end"])
        print("Chromosome name --> " + response_dict["name"])
    except KeyError:
        print("THE DATA INTRODUCED IS WRONG!!\n")

def print_json_function_6(response_dict):
    print("\n++++++++++++++++++++++++++++++++++")
    print("Testing MEDIUM LEVEL-CalcSequence")
    print("++++++++++++++++++++++++++++++++++")
    try:
        print("The GENE selected --> " + response_dict["seq_name"])
        for n in response_dict["count"].keys():
            print(n + " = " + str(response_dict["count"][n]) + "(" + str(response_dict["percentage"][n])+ "%)")
    except:
        print("THE DATA INTRODUCED IS WRONG!!\n")




