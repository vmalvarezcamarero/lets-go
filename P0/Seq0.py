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

def seq_reverse(seq):
    return "".join(reversed(seq))

def seq_complement(seq):
    new_seq = ""
    for base in range(0, len(seq)):
        if seq[base] == "A":
            new_seq += "T"
        elif seq[base] == "C":
            new_seq += "G"
        elif seq[base] == "T":
            new_seq += "A"
        elif seq[base] == "G":
            new_seq += "C"
    return new_seq