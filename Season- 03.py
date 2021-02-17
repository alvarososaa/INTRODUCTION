
def sequence(seq):
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    l = len(seq)
    for element in seq:
        if element == "A":
            countA += 1
        elif element == "C":
            countC += 1
        elif element == "G":
            countG += 1
        elif element == "T":
            countT += 1
    return countA , countC , countG , countT
seq = input("Please enter the sequence you want")
countA, countC, countG , countT = sequence(seq)
# This is useful for making the loops more eficent.
def printed():
    print(countA)
    print(countC)
    print(countG)
    print(countT)
printed()
def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        new_dna = dna.replace("\n", "")
        for element in new_dna:
            ...

x = read_from_file("dna.text")
print(x)








