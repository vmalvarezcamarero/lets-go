from Seq1 import Seq
import jinja2
import pathlib
FOLDER = "../P0/Session-04/"

def print_colored(message, color):
    import colorama
    import termcolor
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

# In order to print colored messages in the python terminal que use the module coloroma, termcolor and colorama.init(strip="False")
# but if we are using the run terminal we only need the module termcolor

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!\n"
    print(response)
    cs.send(str(response).encode())

def get(list, arg):

    context = {
        "number": arg,
        "sequence": list[int(arg)]
    }
    contents = read_template_html_file("./html/GET.html").render(context = context)
    return contents


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


def info(cs, arg):
    list_bases = ["A", "C", "G", "T"]
    print_colored("INFO", "yellow")
    sequence = Seq(arg)
    print("Sequence:", sequence)
    print("Total length:", sequence.len())
    cs.send(("Sequence: " + str(sequence) + "\n" + "Total length: " + str(sequence.len()) + "\n").encode())
    for i in range (0, len(list_bases)):
        print(f'{list_bases[i]}: {sequence.count_base_2()[i]} ({sequence.base_percentage()[i]})')
        cs.send((list_bases[i] + ": " + str(sequence.count_base_2()[i]) + " (" + sequence.base_percentage()[i] + ")").encode())
    print()

def comp(cs, arg):
    print_colored("COMP", "yellow")
    sequence = Seq(arg)
    response = sequence.seq_complement()
    print(response + "\n")
    cs.send(response.encode())

def rev(cs, arg):
    print_colored("REV", "yellow")
    sequence = Seq(arg)
    response = sequence.seq_reverse()
    print(response + "\n")
    cs.send(response.encode())

def gene(arg):
    PATH = "Sequences/" + arg + ".txt"
    s1 = Seq()

    context = {
        "gene_name": arg,
        "gene_content": s1.read_fasta(PATH)
    }
    contents = read_template_html_file("./html/GENE.html").render(context=context)
    return contents

