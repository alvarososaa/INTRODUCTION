import Seq0

FOLDER = "./SEQUENCES/"
id = "U5.txt"
x = Seq0.seq_dna_fasta(FOLDER + id)
print("The first 20 basis are: ", x[0:20])
