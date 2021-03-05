from Seq1 import Seq
print("-------EXCERSISE 7 -------")
gen = Seq()
gen_1 = Seq("ATATATGGT")
gen_2 = Seq("Invalid Sequence")
print(f"Sequence 1: (LENGTH: {gen.length()}) {gen} \n{gen.count()} \nREV: {gen.reversed()}")
print(f"Sequence 2 : (LENGTH {gen_1.length()}) {gen_1} \n{gen_1.count()} \nREV : {gen_1.reversed()}")
print(f"Sequence 3: (LENGTH {gen_2.length()}) {gen_2} \n{gen_2.count()} \nREV: {gen_2.reversed()}")