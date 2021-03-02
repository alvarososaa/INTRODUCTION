class Seq:
    """A class for representing sequences"""
    def __init__(self , strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__(self):
        # Method called for printing the things , siempre que imprimamos algo se ejecuta esto
        return self.strbases
    def len(self):
        return len(self.strbases)
class Gene(Seq):      #Esta sería la clase hija de la anterior, se pone entre parentesis la clase a la que pertence
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass


# Main program
# Create an object of the class Seq
s1 = Seq("AGTACCACTGGT")
g = Gene("CGCTAAC")
print(f"Sequence 1: {s1}") #Esa f sirve para poder poner variables dentro de la string, esas variables se ponen entre parentesos
print(f"Length: {s1.len()}")
print(f"Sequence 2: {g}")
print(f"Length: {g.len()}") #Esta es la manera para obtener los propios resultados

