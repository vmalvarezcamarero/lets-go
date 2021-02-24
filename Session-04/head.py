from pathlib import Path
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
f = file_contents[0:file_contents.find("\n")]
print(f)