import http.server
import socketserver
import termcolor
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
import json
import server_utiles as su

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

LIST_SEQUENCES = ["AAAAAAAAAATTGGCCT", "ACCACAAATGGGGGGTCA", "AAAAATGGGCCTG", "TTTTTTGGGGGTGGGG", "ATGC"]

LIST_GENES =["ADA", "FXN", "PRAT1", "RNU6_269P", "U5"]
# Define the Server's port
PORT = 8080
LIST_OPTIONS = ["Info", "Comp", "Rev"]



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

        SERVER = "rest.ensembl.org"
        PARAMETERS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)

        context = {}

        if path_name == "/":
            contents = read_template_html_file("./html/index.html").render()
        elif path_name.split("?")[0] == "/ListSpecies":
            try:
                ENDPOINT = "/info/species"
                connection.request("GET", ENDPOINT + PARAMETERS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                count = len(response_dict["species"])
                empty_list = []
                for n in range(0, int(arguments["limit"][0])):
                    empty_list.append(response_dict["species"][n]["common_name"])


                context = {"number_seq": count,
                           "limit": arguments["limit"][0],
                           "names": empty_list}

                contents = read_template_html_file("./html/ListSequence.html").render(context=context)

            except ValueError:
                contents = read_template_html_file("./html/DataError.html").render()
        elif path_name.split("?")[0] == "/karyotype":
            try:
                ENDPOINT = "/info/assembly/"
                specie = arguments["specie"][0]
                connection.request("GET", ENDPOINT + specie + PARAMETERS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                print("The dictionary:" + str(response_dict))
                empty_list = []
                for n in response_dict["karyotype"]:
                    empty_list.append(n)

                context = {"kar": empty_list}

                contents = read_template_html_file("./html/Karyotype.html").render(context = context)
            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()

        elif path_name.split("?")[0] == "/chromosomeLength":
            try:
                ENDPOINT = "/info/assembly/"
                specie = arguments["specie"][0]
                connection.request("GET", ENDPOINT + specie + PARAMETERS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                for n in range (0, len (response_dict['top_level_region'])):
                    if response_dict['top_level_region'][n]["name"] == arguments["chromosome"][0]:
                        length = response_dict['top_level_region'][n]["length"]
                        context = {"length": length}
                    else:
                        pass
                    print(response_dict)

                    contents = read_template_html_file("./html/chromosomeLength.html").render(context = context)
            except KeyError:
                contents = read_template_html_file("./html/DataError.html").render()
            except IndexError:
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