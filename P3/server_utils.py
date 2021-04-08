from Seq1 import Seq

def print_colored(message, color):
    import termcolor
    termcolor.cprint(message , color)
def ping():
     print_colored("Ping command", "green")
def sequence(seq):
    aux_string = ""
    basis_counter = seq.count()
    for key, value in basis_counter.items():
        aux_string += f"{key}: {int(value)}   ({(round((value / seq.length() * 100), 2))})\n"
    return f"TOTAL LENGTH: {seq.length()}\n{aux_string}"


