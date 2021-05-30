import http.client
import json
import Seq1
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
ENDPOINT = "/sequence/id/"

connection = http.client.HTTPConnection(SERVER)
try:
    for n in GENE_DICT:
        ID = GENE_DICT[n]
        connection.request("GET", ENDPOINT + ID + PARAMETERS)
        response = connection.getresponse()


        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            sequence = Seq1.Seq(response_dict["seq"])
            s_length = sequence.len()
            bases = sequence.count_bases_6()[0]
            percentage = sequence.count_bases_6()[1]
            most_frequent = sequence.frequent_base(sequence.count_bases_6()[0])
            print("Gene:", n)
            print("Total length: " + str(s_length))
            for n in bases:
                print(n + " --> " + str(bases[n]) + "(" + str(percentage[n]) + "%)")
            print("Most frequent base: " + str(most_frequent))



except KeyError:
    print("The gene is not inside our dictionary. Choose one of the following:", list(GENE_DICT.keys()))