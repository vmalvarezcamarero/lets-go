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


def info(arg):
    list_bases = ["A", "C", "G", "T"]
    sequence = Seq(arg)
    a = sequence.count_bases_6()[0]
    b = sequence.count_bases_6()[1]
    context = {
        "sequence": arg,
        "length": sequence.len(),
        "operation": "Info",
        "bases": a,
        "percentage": b,
        "list": list_bases
    }
    contents = read_template_html_file("./html/INFO.html").render(context=context)
    return contents


def comp(arg):
    sequence = Seq(arg)
    response = sequence.seq_complement()
    context = {
        "sequence": arg,
        "composition": response,
        "operation": "comp"
    }
    contents = read_template_html_file("./html/COMP.html").render(context=context)
    return contents

def rev(arg):
    sequence = Seq(arg)
    response = sequence.seq_reverse()
    context = {
        "sequence": arg,
        "reverse": response,
        "operation": "rev"
    }
    contents = read_template_html_file("./html/REV.html").render(context=context)
    return contents


def gene(arg):
    PATH = "Sequences/" + arg + ".txt"
    s1 = Seq()

    context = {
        "gene_name": arg,
        "gene_content": s1.read_fasta(PATH)
    }
    contents = read_template_html_file("./html/GENE.html").render(context=context)
    return contents

