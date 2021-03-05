from Seq1 import Seq
print("-------EXCERSISE 9 and 10-------")
FOLDER = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P0/SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
for g in gene_list:
    gen = Seq(Seq.read_fasta(FOLDER + g + ".txt"))
    print(f"{g}: (LENGTH: {gen.length()}) {gen} \n{gen.count()} \nREV: {gen.reversed()} \nCOMPL: {gen.complement()}")

