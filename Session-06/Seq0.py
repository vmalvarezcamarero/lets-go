class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        self.strbases = strbases

        if self.sequence_is_valid():
            self.strbases = strbases
            print("New sequence created")
        else:
            self.strbases = "ERROR"
            print("INCORRECT Sequence detected!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def sequence_is_valid(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

    @staticmethod
    def print_bases(list_sequences):
        for a in range(0,len(list_sequences)):
            print(f"Sequence {a} (Length:{list_sequences[a].len()}):{list_sequences[a]}")

def generate_series(sequ, number):
    li = []
    for i in range(0, number):
        li.append(Seq(sequ * (i + 1)))
    return li