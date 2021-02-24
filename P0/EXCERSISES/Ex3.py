import Seq0
GENE_FOLDER = "../SEQUENCES/"
gene_list = ["U5", "FRAT1"]
print("EXCERSISE 3:")
for gene in gene_list:
    sequence = Seq0.seq_dna_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene" + gene + " ---> Length: ", + Seq0.seq_len(sequence))