class Seq:

    def __init__(self, strbases):

        self.strbases = strbases

    def __str__(self):

        return self.strbases

    def len(self):

        return len(self.strbases)


def print_seqs(seq_list):

    for s in range(0,len(seq_list)):
        print(f"Sequence {s} (Length: {seq_list[s].len()}): {seq_list[s]}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)