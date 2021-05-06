from Seq1 import Seq , generate_series
print("-----| Practice 1, Exercise 4 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1 (Length:{s1.len()}): {s1}")
print(f"Sequence 2 (Length:{s2.len()}): {s2}")
print(f"Sequence 3 (Length:{Seq.len(s3)}): {s3}")