from Seq1 import Seq
print("------EXCERSISE 5-------")
gen = Seq()
gen_1 = Seq("ATATAT")
gen_2 = Seq("Invalid Sequence")
print(f"Sequence 1: (LENGTH: {gen.length()}) {gen} \nA: {gen.count_bases()[0]} C: {gen.count_bases()[1]} G: {gen.count_bases()[2]} T: {gen.count_bases()[3]}")
print(f"Sequence 2 : (LENGTH {gen_1.length()}) {gen_1} \nA: {gen_1.count_bases()[0]} C: {gen_1.count_bases()[1]} G: {gen_1.count_bases()[2]} T: {gen_1.count_bases()[3]}")
print(f"Sequence 3: (LENGTH {gen_2.length()}) {gen_2} \nA: {gen_2.count_bases()[0]} C: {gen_2.count_bases()[1]} G: {gen_2.count_bases()[2]} T: {gen_2.count_bases()[3]}")