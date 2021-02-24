import P0.Seq0 as Seq0
gene_folder = "./Sequences/"
gene_list = ["U5", "ADA", "PRAT1", "FXN"]
b = ["A", "C", "T", "G"]

print("-----| Exercise 4 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("Gene " + gene)
    for base in b:
        bases = Seq0.seq_count_base(sequence, base)
        print(base + ":", bases)