from pathlib import Path


def seq_ping():
    print("OK")
    print("You have created your first module.")

def take_out_first_line(sequence):
    return sequence[sequence.find("\n") + 1:].replace("\n", "")

def seq_dna_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence
def seq_len(sequence):
    return len(sequence)
def count_basis(sequence, basis):
    return sequence.count(basis)
def seq_counts(sequence):
    a,c,g,t = 0,0,0,0
    for d in sequence:
        if d == "A":
            a+= 1
        elif d == "C":
            c += 1
        elif d == "G":
            g += 1
        else:
            t += 1
    return {"A": a, "C": c, "G" : g, "T": t}
def seq_complement(sequence):
    complement_string = ""
    for d in sequence:
        if d == "A":
            complement_string += "T"
        elif d == "C":
            complement_string += "G"
        elif d == "G":
            complement_string += "C"
        else:
            complement_string += "A"
    return complement_string

def most_commom_base(sequence):
    number_list = []
    base_list = []
    for number in seq_counts(sequence).values():
        number_list.append(number)
    for base in seq_counts(sequence).keys():
        if max(number_list) == seq_counts(sequence)[base]:
            base_list.append(base)
    return base_list











