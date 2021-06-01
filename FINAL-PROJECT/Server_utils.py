from jinja2 import Template
import pathlib
import http.client
import json
import Seq1 as Seq
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/FINAL-PROJECT/HTML"
def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content
def species_list(response, limit=None):
    species_list = []
    if limit == None or limit > len(response["species"]):
        for element in response["species"]:
            species_list.append(element["display_name"])
    else:
        for element in response["species"][0: int(limit)]:
            species_list.append(element["display_name"])
    context = {"Species": species_list,
               "limit": limit}
    contents = read_template_html_file(ROOT + "/species.html").render(context=context)
    return contents
def api_connection(ENDPOINT, PARAMS, SERVER):
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    response = json.loads(response.read().decode())
    return response
def chromosome_length(response, specie, chromosome_number):
    try:
        x = response["top_level_region"]
        for chromosome_information in x:
            if chromosome_information["name"] == chromosome_number:
                length = chromosome_information["length"]
        context = {"Specie": specie,
                   "chromosome_number" : chromosome_number,
                   "Length": length}
        contents = read_template_html_file(ROOT + "/length.html").render(context=context)
        return contents
    except UnboundLocalError:
        contents = read_template_html_file(ROOT + "/ERROR.html").render()
        return contents
def calculations(response, ID):
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
    contents = read_template_html_file(ROOT + "/info.html").render(context=context)
    return contents
def second_calculations(response, ID):
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
    contents = read_template_html_file(ROOT + "/calc.html").render(context=context)
    return contents









