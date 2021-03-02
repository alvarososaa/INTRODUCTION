class Seq:
    def __init__(self , sequence):
        self.sequence = sequence
    def __str__(self):
        return self.sequence
    def correct_sequence(self):
        counter = 0
        for element in self.sequence:
            if element != "A" and element != "C" and element != "G" and element != "T":
                counter += 1
            else:
                pass
        if counter > 0:
             return "Sorry , the sequence is incorrect"
        else:
            return "The sequence is correct"
    def length(self):
        return len(self.sequence)
class generator(Seq):
    def __init__(self , pattern , number):
        self.pattern = pattern
        self.number = number
    def seq_generator(self):
        lista = []
        for n in range(1 , self.number + 1):
            print("New sequence created")
            lista.append((self.pattern) * n)
        return lista



#seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
#for element in range(0, len(seq_list)):
    #print(f"Sequence {element + 1} :  {seq_list[element]} {seq_list[element].length()}")
gene = generator("ABCD" , 8)
for element in gene.seq_generator():
    print(f" Sequence : {element} {Seq(element).length()}")
