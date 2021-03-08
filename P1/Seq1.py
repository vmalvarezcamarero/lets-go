class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        self.strbases = strbases
        if strbases == "NULL":
            print("NULL sequence created")
            self.strbases = strbases
        else:

            if self.sequence_is_valid():
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("INCORRECT Sequence detected!")

    def __str__(self):
        if self.strbases != "NULL":
            return self.strbases
        else:
            return "NULL"

    def sequence_is_valid(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases != "NULL" and self.strbases != "ERROR":
            return len(self.strbases)
        else:
            return 0

    @staticmethod
    def print_bases(list_sequences):
        for a in range(0,len(list_sequences)):
            print(f"Sequence {a} (Length:{list_sequences[a].len()}):{list_sequences[a]}")

    def count_bases(self):
        if self.strbases != "ERROR" and self.strbases != "NULL":
            print(f" A: {self.strbases.count('A')}, C: {self.strbases.count('C')}, T: {self.strbases.count('T')}, G: {self.strbases.count('G')},")
        else:
            print(f" A: 0, C: 0, T: 0, G: O,")

def generate_series(sequ, number):
    li = []
    for i in range(0, number):
        li.append(Seq(sequ * (i + 1)))
    return li