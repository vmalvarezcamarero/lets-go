class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        self.strbases = strbases

        for a in strbases:
            if a != "A" and a != "C" and a != "G" and a != "T":
                self.strbases = ("ERROR")

                print("There has been an ERROR!")
                break

            else:
                self.strbases = strbases

    print("New sequence created ")



    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence



        return self.strbases




s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

