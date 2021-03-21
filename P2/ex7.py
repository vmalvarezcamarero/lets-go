from Client0 import Client
from Client import Client1
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
c1 = Client1(IP, 8081)
s = Seq()
s.read_fasta("P2/Sequences/PRAT1.txt")
print(f"Gene FRAT1: {s}")
count = 0
i = 0
while i < len(s.strbases) and count < 10:
    print(f"Fragment {count + 1} : {s.strbases[i:i + 10]}")
    count += 1
    i += 1
    if count % 2 != 0:
        print(c.talk(f"Fragment {count} : {s.strbases[i:i + 10]}" ))
    elif count % 2 == 0:
        print(c1.talk(f"Fragment {count} : {s.strbases[i:i + 10]}" ))
    else:
        break
