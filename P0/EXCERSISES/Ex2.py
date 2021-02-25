import Seq0

FOLDER = "./SEQUENCES/"
gene_list = ["U5", "FRAT1", "RNU6_269P", "FXN", "ADA"]
for gene in gene_list:
    x = Seq0.seq_dna_fasta(FOLDER + gene + ".txt")
    print("The first 20 basis for the gene " , gene, " are: ", x[0:20])
