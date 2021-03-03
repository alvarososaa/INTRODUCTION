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
    @staticmethod
    def sequence_list(seq_list):
        for i in range(0 , len(seq_list)):
            print(f"Sequence {i + 1} : {seq_list[i]} {Seq(seq_list[i]).length()}  ")



seq_list = ["AGAGA" , "ATATA" , "ACACACA"]
Seq.sequence_list(seq_list)
for element in seq_list:
    print(Seq(element).sequence)

