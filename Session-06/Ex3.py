from Seq0 import Seq , generate_series

seq_list1 = generate_series("A", 3)
seq_list2 = generate_series("AC", 5)
print("List 1:")
Seq.print_bases(seq_list1)

print()
print("List 2:")
Seq.print_bases(seq_list2)