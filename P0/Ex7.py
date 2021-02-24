import P0.Seq0 as Seq0
FOLDER = "./Sequences/U5.txt"
U5_Seq = Seq0.seq_read_fasta(FOLDER)

print("-----| Exercise 7 |------")
print("Gene U5:")
print ("Frag:" + U5_Seq[0: 20])
print ("Comp:" + str(Seq0.seq_complement(U5_Seq[0: 20])))