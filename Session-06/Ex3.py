def len_(seq_list):
    return len(seq_list)

def generate_seqs(seq, number):
    l = []
    for a in range(0, number):
        l.append(seq + a*seq)
    return l


def print_seqs(seq_list):
    for s in range(0,len(seq_list)):
        print(f" sequence {s} (length : {len_(seq_list[s])}): {seq_list[s]}")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)
print(seq_list1)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)