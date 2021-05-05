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
def rev(sequence):
    return sequence[::-1]

def operations(sequence, operation):
    if operation == "REV":
        seq = rev(sequence)
    elif operation == "INFO":
        seq = info(sequence)
    else:
        seq = compl(sequence)
    context = {"normal_sequence": sequence,
               "operated_sequence": seq,
               "op": operation}
    if operation == "INFO":
        contents = read_template_html_file(ROOT + "/info.html").render(context=context)
    else:
        contents = read_template_html_file(ROOT + "/OPERATIONS.html").render(context=context)
    return contents

def compl(sequence):
    COMPL = ""
    for element in sequence:
        if element == "A":
            COMPL += "T"
        elif element == "G":
            COMPL += "C"
        elif element == "C":
            COMPL += "G"
        else:
            COMPL += "T"
    return COMPL
def info(seq):
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")
    counterA = (round(seq.count("A") / len(seq),2)) * 100
    counterC = (round(seq.count("C") / len(seq), 2)) * 100
    counterG = (round(seq.count("G") / len(seq), 2)) * 100
    counterT = (round(seq.count("T") / len(seq), 2)) * 100
    return [len(seq), {"A: " : counterA, "C:" : counterC, "G:" : counterG, "T: " : counterT}]






