from pathlib import Path
class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):

        self.strbases = strbases
        if strbases == Seq.NULL_SEQUENCE:
            self.strbases = strbases
        else:

            if self.sequence_is_valid():
                self.strbases = strbases

            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected!")

    def __str__(self):
        if self.strbases != Seq.NULL_SEQUENCE:
            return self.strbases
        else:
            return Seq.NULL_SEQUENCE

    def sequence_is_valid(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases != Seq.NULL_SEQUENCE and self.strbases != Seq.INVALID_SEQUENCE:
            return len(self.strbases)
        else:
            return 0


    @staticmethod
    def print_bases(list_sequences):
        for a in range(0,len(list_sequences)):
            print(f"Sequence {a} (Length:{list_sequences[a].len()}):{list_sequences[a]}")

    def read_fasta(self, filename):
        sequence = Path(filename).read_text()
        sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
        self.strbases = sequence
        return sequence

    @staticmethod
    def frequent_base(dict):
        maximum = max(dict.values())
        for key, value in dict.items():
            if value == maximum:
                return key


    def count_bases(self):

        if self.strbases != Seq.INVALID_SEQUENCE and self.strbases != Seq.NULL_SEQUENCE:
            a = self.strbases.count('A') / (self.strbases.count('A') + self.strbases.count('C') + self.strbases.count('T') + self.strbases.count('G'))*100
            c = self.strbases.count('C') / (self.strbases.count('A') + self.strbases.count('C') + self.strbases.count('T') + self.strbases.count('G'))*100
            t = self.strbases.count('T') / (self.strbases.count('A') + self.strbases.count('C') + self.strbases.count('T') + self.strbases.count('G'))*100
            g = self.strbases.count('G') / (self.strbases.count('A') + self.strbases.count('C') + self.strbases.count('T') + self.strbases.count('G'))*100


            return f"A: {self.strbases.count('A')} ({round(a, 2)}%) \nC: {self.strbases.count('C')} ({round(c,2)}%) \nT: {self.strbases.count('T')} ({round(t,2)}%) \nG: {self.strbases.count('G')} ({round(g,2)}%)"
        else:
            print(f" A: 0, C: 0, T: 0, G: O,")
    def create_dict(self):
        if self.strbases != Seq.INVALID_SEQUENCE and self.strbases != Seq.NULL_SEQUENCE:
            return{"A": self.strbases.count('A'), "C": self.strbases.count('C'), "T": self.strbases.count('T'), "G": self.strbases.count('G'),}
        else:
            return{"A": 0, "C": 0, "T": 0, "G": 0,}

    def seq_reverse(self):
        if self.strbases != Seq.INVALID_SEQUENCE and self.strbases != Seq.NULL_SEQUENCE:
            return "".join(reversed(self.strbases))
        else:
            return self.strbases

    def seq_complement(self):
        new_seq = ""
        if self.strbases != Seq.INVALID_SEQUENCE and self.strbases != Seq.NULL_SEQUENCE:
            for base in range(0, len(self.strbases)):
                if self.strbases[base] == "A":
                    new_seq += "T"
                elif self.strbases[base] == "C":
                    new_seq += "G"
                elif self.strbases[base] == "T":
                    new_seq += "A"
                elif self.strbases[base] == "G":
                    new_seq += "C"
            return new_seq
        else:
            return self.strbases
    def count_bases_6(self):
        a, c, g, t= 0, 0, 0, 0
        for e in self.strbases:
            if e == "A":
                a += 1
            elif e == "C":
                c += 1
            elif e == "G":
                g += 1
            elif e == "T":
                t += 1
        new_dict = {"A": a,"C": c,"G": g,"T": t}
        percentage = {"A": round((a / (a+c+g+t))*100, 2), "C": round((c / (a+c+g+t))*100,2), "G": round((g / (a+c+g+t))*100,2), "T": round((t / (a+c+g+t))*100,2)}
        return new_dict, percentage

def generate_series(sequ, number):
    li = []
    for i in range(0, number):
        li.append(Seq(sequ * (i + 1)))
    return li