import P0.Seq0 as Seq0
gene_folder = "./Sequences/"
U5 = "U5"
ADA = "ADA"
PRAT1 = "PRAT1"
FXN = "FXN"
base = ["A", "C", "G", "T"]


sequence_U5 = Seq0.seq_read_fasta(gene_folder + U5 + ".txt")
bases = Seq0.seq_count(sequence_U5)
l_U5 = []
for a in bases:
    l_U5.append(bases[a])
    U5_h = l_U5.index(max(l_U5))

sequence_ADA = Seq0.seq_read_fasta(gene_folder + ADA + ".txt")
bases2 = Seq0.seq_count(sequence_ADA)
l_ADA = []
for b in bases2:
    l_ADA.append(bases2[b])
    ADA_h = l_ADA.index(max(l_ADA))

sequence_PRAT1 = Seq0.seq_read_fasta(gene_folder + PRAT1 + ".txt")
bases3 = Seq0.seq_count(sequence_U5)
l_PRAT1 = []
for c in bases3:
    l_PRAT1.append(bases3[c])
    PRAT1_h = l_PRAT1.index(max(l_PRAT1))

sequence_FXN = Seq0.seq_read_fasta(gene_folder + FXN + ".txt")
bases4 = Seq0.seq_count(sequence_FXN)
l_FXN = []
for d in bases4:
    l_FXN.append(bases4[d])
    FXN_h = l_FXN.index(max(l_FXN))

print("-----| Exercise 8 |------")
print ("The most common base of the gene", U5, "is: --|" ,base[U5_h], "|--")
print ("The most common base of the gene", ADA, "is: --|" ,base[ADA_h], "|--")
print ("The most common base of the gene", PRAT1, "is: --|" ,base[PRAT1_h], "|--")
print ("The most common base of the gene", FXN, "is: --|" ,base[FXN_h], "|--")

