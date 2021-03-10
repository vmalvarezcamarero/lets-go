from Seq1 import Seq
gene_folder = "Sequences/"

l = ["U5", "ADA", "FXN", "PRAT1", "RNU6_269P" ]

for a in l:
    s = Seq()
    s.read_fasta(gene_folder + a + ".txt")
    print(f"Gene {a} Most frequent Base:{s.frequent_base(s.create_dict())}")
