from pathlib import Path

sequence = Path("f1.txt").read_text()
a = sequence.replace("\n", "")
count = 0
for b in a:
    count += 1
print(count)

