import termcolor
from pathlib import Path
class Seq:
    def __init__(self, sequence="NULL"):
        if sequence == "NULL":
            print("NULL SEQUENCE CREATED")
            self.sequence = sequence

        else:
            if Seq.is_valid_sequence_2(sequence):
                print("NEW SEQUENCE CREATED")
                self.sequence = sequence
            else:
                self.sequence = "ERROR"
                print("INVALID SEQUENCE CREATED")

    @staticmethod
    def is_valid_sequence_2(sequence):
        for c in sequence:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.sequence == "ERROR" or self.sequence == "NULL":
            return a, c, g, t
        else:
            for element in self.sequence:
                if element == "A":
                    a += 1
                elif element == "C":
                    c += 1
                elif element == "G":
                    g += 1
                else:
                    t += 1
            return a, c, g, t


    def reversed(self):
        if self.sequence == "ERROR" or self.sequence == "NULL":
            return self.sequence
        else:
            return self.sequence[::-1]

    def read_fasta(self, filename):
        sequence = Path(filename).read_text()
        genome = sequence[sequence.find("\n") + 1:].replace("\n", "")
        self.sequence = genome
        return self.sequence

    def most_common_base(self):
        value_string = ""
        lista = []

        for element in Seq.count(self).values():
            lista.append(element)
        for key in Seq.count(self).keys():
            if Seq.count(self)[key] == max(lista):
                value_string += key
        return value_string





    def complement(self):
        aux_string = ""
        if self.sequence == "ERROR" or self.sequence == "NULL":
            return self.sequence
        else:
            for element in self.sequence:
                if element == "A":
                    aux_string += "T"
                elif element == "G":
                    aux_string += "C"
                elif element == "C":
                    aux_string += "G"
                else:
                    aux_string += "A"
            return aux_string



    def count(self):
        a, c, g, t = 0, 0, 0, 0
        if self.sequence == "ERROR" or self.sequence == "NULL":
            return {"A": a, "C": c, "G": g , "T": t}
        else:
            for element in self.sequence:
                if element == "A":
                    a += 1
                elif element == "C":
                    c += 1
                elif element == "G":
                    g += 1
                else:
                    t += 1
            return {"A": a, "C": c, "G": g , "T": t}






    def __str__(self):
        return self.sequence
    def length(self):
        if self.sequence == "NULL" or self.sequence == "ERROR":
            return 0
        else:
             return len(self.sequence)