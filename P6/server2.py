import http.server
import socketserver
import termcolor


from urllib.parse import urlparse, parse_qs
import server_utiles as su

LIST_SEQUENCES = ["AAAAAAAAAATTGGCCT", "ACCACAAATGGGGGGTCA", "AAAAATGGGCCTG", "TTTTTTGGGGGTGGGG", "ATGC"]

LIST_GENES =["ADA", "FXN", "PRAT1", "RNU6_269P", "U5"]
# Define the Server's port
PORT = 8080
LIST_OPTIONS = ["Info", "Comp", "Rev"]
Basis_inf = {
    "A":{"link": "https://es.wikipedia.org/wiki/Adenina",
         "formula": "C5H5N5",
         "name": "ADENINE",
         "colour": "lightgreen"},
    "C":{"link": "https://es.wikipedia.org/wiki/Cytosine",
         "formula": "C5Hu5N5",
         "name": "CYTOSINE",
         "colour": "lightblue"},
    "G":{"link": "https://es.wikipedia.org/wiki/Adenina",
         "formula": "C5Hw5N5",
         "name": "GUANINE",
         "colour": "yellow"},
    "T":{"link": "https://es.wikipedia.org/wiki/Adenina",
         "formula": "C5Hh5N5",
         "name": "THYMINE",
         "colour": "pink"}

}
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the clinet


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        print("The path we have followed --> " + self.path)
        context = {}

        if path_name == "/":
            context["n_sequences"] = len(LIST_SEQUENCES)
            context["list_genes"] = LIST_GENES
            context["n_option_name"] = len(LIST_OPTIONS)
            context["option_name"] = LIST_OPTIONS
            contents = su.read_template_html_file("./html/index.html").render(context=context)

        elif path_name == "/ping":
            contents = su.read_template_html_file("./html/PING.html").render()
        elif path_name == "/get":
            number_sequence = arguments["sequence"][0]
            contents = su.get(LIST_SEQUENCES, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name =="/operation":
            if arguments["operation"][0] == "Info":
                contents = su.info(arguments["sequence"][0])
            elif arguments["operation"][0] == "Comp":
                contents = su.comp(arguments["sequence"][0])
            elif arguments["operation"][0] == "Rev":
                contents = su.rev(arguments["sequence"][0])
            else:
                contents = su.read_template_html_file("./html/Error.html").render()
        else:
            contents = su.read_template_html_file("./html/Error.html").render()


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