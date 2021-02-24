import Seq0

GENE_FOLDER = "../SEQUENCES/"
gene_list = ["U5", "FRAT1"]
base_list =["A", "C", "T", "G"]
print("EXCERSISE 4: ")
for gene in gene_list:
    sequence = Seq0.seq_dna_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene)
    for base in base_list:
        Seq0.count_basis(sequence, base)

