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

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

