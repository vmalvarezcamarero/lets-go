from Seq1 import Seq
FILENAME = "Sequences/U5.txt"
s = Seq()
s.read_fasta(FILENAME)

print(f"Sequence 1 (Length:{Seq.len(s)}): {s}\n Bases: {Seq.create_dict(s)}\n Rev: {Seq.seq_reverse(s)}\n Comp: {Seq.seq_complement(s)}")
