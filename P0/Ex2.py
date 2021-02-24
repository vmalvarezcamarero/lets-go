import P0.Seq0 as Seq0
FOLDER = "../Session-04/U5.txt"
ID = "U5.txt"
U5_Seq = Seq0.seq_read_fasta(FOLDER)
print("The first 20 bases are:", U5_Seq[0:20])
print (U5_Seq)