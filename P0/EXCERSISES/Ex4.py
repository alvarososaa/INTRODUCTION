import Seq0

GENE_FOLDER = "../SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
base_list =["A", "C", "T", "G"]
print("EXCERSISE 4: ")
for gene in gene_list:
    sequence = Seq0.seq_dna_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene)
    for base in base_list:
        print(base," ----->", Seq0.count_basis(sequence, base))


