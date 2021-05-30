import http.server
import socketserver
import termcolor
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
import Utiles as Us

GENE_DICT = {"FRAT1":"ENSG00000165879",
     "ADA":"ENSG00000196839",
     "FXN":"ENSG00000165060",
     "RNU6_269P":"ENSG00000212379",
     "MIR633":"ENSG00000207552",
     "TTTY4C":"ENSG00000226906",
     "RBMY2YP":"ENSG00000227633",
     "FGFR3":"ENSG00000068078",
     "KDR":"ENSMUSG00000062960",
     "ANK2":"ENSG00000145362"
}

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

LIST_SEQUENCES = ["AAAAAAAAAATTGGCCT", "ACCACAAATGGGGGGTCA", "AAAAATGGGCCTG", "TTTTTTGGGGGTGGGG", "ATGC"]

LIST_GENES =["ADA", "FXN", "PRAT1", "RNU6_269P", "U5"]
PORT = 8080
LIST_OPTIONS = ["Info", "Comp", "Rev"]

context = {}
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')


        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        self.send_response(200)  # -- Status line: OK!
        print("The path we have followed --> " + self.path)


        if path_name == "/":
            contents = read_template_html_file("./html/index.html").render()

        elif path_name.split("?")[0] == "/listSpecies":
            try:
                if int(arguments["limit"][0]) <= 310 and int(arguments["limit"][0]) >= 0:
                    contents = read_template_html_file("./html/ListSequence.html").render(context=dict(Us.function_1(arguments)))

                elif int(arguments["limit"][0]) >= 310:
                    contents = read_template_html_file("./html/ListSequence.html").render(context=dict(Us.function_2(arguments)))

            except ValueError:
                contents = read_template_html_file("./html/DataError.html").render()

        elif path_name.split("?")[0] == "/karyotype":
            try:
                contents = read_template_html_file("./html/Karyotype.html").render(context=dict(Us.function_3(arguments)))

            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()

        elif path_name.split("?")[0] == "/chromosomeLength":
            try:
                contents = read_template_html_file("./html/chromosomeLength.html").render(context=dict(Us.function_4(arguments)))

            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()

            except IndexError:
                contents = read_template_html_file("./html/DataError.html").render()

            except TypeError:
                contents = read_template_html_file("./html/DataError.html").render()

        elif path_name.split("?")[0] == "/geneSeq":
            try:
                contents = read_template_html_file("./html/Gene_Seq.html").render(context=dict(Us.function_5(arguments)))

            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()

        elif path_name.split("?")[0] == "/geneInfo":
            try:
                contents = read_template_html_file("./html/Gene_Info.html").render(context=dict(Us.function_6(arguments)))

            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()


        elif path_name.split("?")[0] == "/geneCalc":
            try:
                contents = read_template_html_file("./html/Gene_basis.html").render(context=dict(Us.function_7(arguments)))

            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()

        else:
            contents = read_template_html_file("./html/Error.html").render()


        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()