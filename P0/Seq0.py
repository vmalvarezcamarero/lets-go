from pathlib import Path
filename = "Sequences/ADA.txt"


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    sequence = Path(filename).read_text()
    sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0
    for n in seq:
        if n == "A":
            a += 1
        elif n == "C":
            c += 1
        elif n == "G":
            g += 1
        elif n == "T":
            t += 1
    return {"A": a, "C": c, "G": g, "T": t}

