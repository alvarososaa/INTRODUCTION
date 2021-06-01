import json
import Seq1 as Seq
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/FINAL-PROJECT/HTML"
SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"
def requesting_connection(path, connection):
    connection.request("GET", path)
    response = connection.getresponse()
    contents = json_connection(response)
    return contents


def json_connection(response):
    if response.status == 200:
        information = response.read().decode("utf-8")
        contents = json.loads(information)
    else:
        contents = "A connection problem occurred"
    return contents
def json_species(response, limit=None):
    species_list = []
    if limit == None or limit > len(response["species"]):
        for element in response["species"]:
            species_list.append(element["display_name"])
    else:
        for element in response["species"][0: int(limit)]:
            species_list.append(element["display_name"])
    context = {"Species": species_list,
               "limit": limit}
    return context
def json_chromosome_length(response, specie, chromosome_number):
    try:
        x = response["top_level_region"]
        for chromosome_information in x:
            if chromosome_information["name"] == chromosome_number:
                length = chromosome_information["length"]
        context = {"Specie": specie,
                   "chromosome_number" : chromosome_number,
                   "Length": length}
        return context
    except UnboundLocalError:
        context = "Sorry the data introduced is bad"
        return context
def json_calculations(response, ID):
    length = len(response["seq"])
    id = response["id"]
    chromosome_name = response["desc"].split(":")[2]
    start = response["desc"].split(":")[3]
    end = response["desc"].split(":")[4]
    context = {"length": length,
               "id": id,
               "chromosome_name": chromosome_name,
               "gene_name": ID,
               "start": start,
               "end": end}
    return context
def json_second_calculations(response, ID):
    length = len(response["seq"])
    sequence = Seq.Seq(response["seq"])
    basis_information = sequence.count()
    A = basis_information["A"]
    C = basis_information["C"]
    G = basis_information["G"]
    T = basis_information["T"]

    context = {"length": length,
               "basis_info": [A, C, G, T],
               "gene_name": ID}
    return context
def print_json(contents):
    if type(contents) == str:
        print(contents)
    else:
        for key, value in contents.items():
            print(key, "----------", value)



def print_json_calculations(contents):
    if type(contents)== str:
        print(contents)
    else:
        print("A------", contents["basis_info"][0][0], contents["basis_info"][0][1], "%")
        print("C------", contents["basis_info"][1][0], contents["basis_info"][1][1], "%")
        print("G------", contents["basis_info"][2][0], contents["basis_info"][2][1], "%")
        print("T------", contents["basis_info"][3][0], contents["basis_info"][3][1], "%")
        print("GENE_NAME------", contents["gene_name"])
        print("LENGTH-------", contents["length"])




