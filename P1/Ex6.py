from Seq1 import Seq , generate_series
print("-----| Practice 1, Exercise 6 |------")
listt = ("A", "C", "T", "G")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1 (Length:{Seq.len(s1)}): {s1}\n {Seq.create_dict(s1)}")
print(f"Sequence 2 (Length:{Seq.len(s2)}): {s2}\n {Seq.create_dict(s2)}")
print(f"Sequence 3 (Length:{Seq.len(s3)}): {s3}\n {Seq.create_dict(s3)}")