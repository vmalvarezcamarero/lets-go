from pathlib import Path
FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
f = file_contents.split("\n")[1:]

A = 0
C = 0
G = 0
T = 0
for e in f:
    for a in e:
        if a == "A":
            A += 1
        if a == "C":
            C += 1
        if a == "G":
            G += 1
        if a == "T":
            T += 1


print("A:", str(A), "C:", str(C), "G:", str(G), "T:", str(T))