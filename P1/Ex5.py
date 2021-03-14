from Seq1 import Seq
def print_result(i,gen):
    print(f"Sequence {i}: (LENGTH: {gen.length()}) {gen}\nA: {gen.count_bases()[0]} C: {gen.count_bases()[1]} G: {gen.count_bases()[2]} T: {gen.count_bases()[3]}")
print("------EXCERSISE 5-------")
gen = Seq()
gen_1 = Seq("ATATAT")
gen_2 = Seq("Invalid Sequence")
gen_list = [gen , gen_1 , gen_2]
for i in range(0, len(gen_list)):
    print_result(i + 1, gen_list[i])
