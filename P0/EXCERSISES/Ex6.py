import Seq0
FOLDER = "../SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
print("------EXCERSISE 6-------")
for gene in gene_list:
    sequence = Seq0.seq_dna_fasta(FOLDER + gene + ".txt")
    print("Gene: ", gene)
    print("FRAG: ", sequence[0:20])
    print("REV: ", sequence[19::-1])