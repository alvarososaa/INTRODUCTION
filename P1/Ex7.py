from Seq1 import Seq
def print_result(i,gen):
    print(f"Sequence {i}: (LENGTH: {gen.length()}) {gen} \n{gen.count()} \nREV: {gen.reversed()}")
print("-------EXCERSISE 7 -------")
gen = Seq()
gen_1 = Seq("ATATATGGT")
gen_2 = Seq("Invalid Sequence")
gen_list = [gen , gen_1 , gen_2]
for i in range(0, len(gen_list)):
    print_result(i + 1, gen_list[i])
