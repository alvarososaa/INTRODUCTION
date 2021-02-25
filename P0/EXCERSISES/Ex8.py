import Seq0
FOLDER = "../SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
print("------EXCERSISE 8------")
for gene in gene_list:
    sequence = Seq0.seq_dna_fasta(FOLDER + gene + ".txt")
    for element in Seq0.most_commom_base(sequence):
        print("Gene: ", gene , ": Most frecuent base: ", element)