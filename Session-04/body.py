from pathlib import Path
FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
f = file_contents.split("\n")
lis = f[1:]
print("The sequence is:")
for e in lis:
    print (e)