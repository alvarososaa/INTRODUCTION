import Seq0
FOLDER = "../SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
print("------EXCERSISE 7------")
for gene in gene_list:
    sequence = Seq0.seq_dna_fasta(FOLDER + gene + ".txt")
    print("Gene: ", gene)
    print("Frag : ", sequence[0:20])
    print("Complement: ", Seq0.seq_complement(sequence[0:20]))
