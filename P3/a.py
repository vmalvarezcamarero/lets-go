from pathlib import Path

def read_fasta(filename):
    sequence = Path(filename).read_text()
    sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return sequence

