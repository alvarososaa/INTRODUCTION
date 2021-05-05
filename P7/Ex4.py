import http.client
import json
import Seq1
gene_dict = {"FRAT1": "ENSG00000165879",
             "ADA": "ENSG00000196839",
             "FXN": "ENSG00000165060",
             "RNU6_269P": "ENSG00000212379",
             "MIR633": "ENSG00000207552",
             "TTTY4C": "ENSG00000228296",
             "RBMY2YP": "ENSG00000227633",
             "FGFR3": "ENSG00000068078",
             "KDR": "ENSG00000128052",
             "ANK2": "ENSG00000145362"
             }
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
connection = http.client.HTTPConnection(SERVER)
try:
    user_gene = input("Enter the gene you want to analyse.")
    id = gene_dict[user_gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        #print(json.dumps(response, indent=4, sort_keys=True))
        sequence = Seq1.Seq(response_dict["seq"])
        s_length = sequence.length()
        most_frequent_base = sequence.most_common_base()
        a, c, g, t = sequence.count_bases()
        print("LENGTH: ", s_length)
        print(a)
        print(c)
        print(g)
        print(t)
except KeyError:
    print("The gene is not available, please choose a correct one.", list(gene_dict.keys()))

