from Seq1 import Seq
print("-------EXCERSISE 10-------")
FOLDER = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P0/SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
for g in gene_list:
    gen = Seq()
    gen.read_fasta(FOLDER + g + ".txt")
    print(f"The most common base is: {gen.most_common_base()}")
