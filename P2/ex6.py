from Client0 import Client
from Client import Client1

from Seq1 import Seq
PRACTICE = 2
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)

s = Seq()
s.read_fasta("P2/Sequences/PRAT1.txt")
print(f"Gene FRAT1: {s}")
count = 0
for i in range(0, len(s.strbases), 10):
    print(f"Fragment {count + 1} : {s.strbases[i:i+10]}")
    print(c.talk(s.strbases[i:i+10]))
    count += 1
    if count == 5:
        break