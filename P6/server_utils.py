from jinja2 import Template
import pathlib
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P6/HTML"
def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content
def get(list_sequences, number):
    context = {"number": number,
               "sequence": list_sequences[number]
               }
    contents = read_template_html_file(ROOT + "/sequence.html").render(context=context)
    return contents
def read_fasta(filename):
    sequence = pathlib.Path(filename).read_text()
    genome = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return genome
def gen(gene):
    filename = read_fasta("/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P6/SEQUENCES/" + gene + ".txt")
    context = {"name": gene,
               "sequence": filename
               }
    contents = read_template_html_file(ROOT + "/gene.html").render(context=context)
    return contents




