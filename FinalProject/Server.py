import http.server
import socketserver
import termcolor
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
import Utiles as Us
import json

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

LIST_GENES =["ADA", "FXN", "PRAT1", "RNU6_269P", "U5"]
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        termcolor.cprint("  The path we have used: " + self.path, "blue")

        # we are creating a parse object (easier way to work with the elements of the path
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)

        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)

        if 'json' in arguments.keys() and arguments["json"][0] == "1":
            inf_type = "application/json"
            try:
                if path_name == "/listSpecies":
                    contents = json.dumps(Us.function_1(arguments), indent=4, sort_keys=True)

                elif path_name == "/karyotype":
                    contents = json.dumps(Us.function_3(arguments), indent=4, sort_keys=True)

                elif path_name == "/chromosomeLength":
                    contents = json.dumps(Us.function_4(arguments), indent=4, sort_keys=True)

                elif path_name == "/geneSeq":
                    contents = json.dumps(Us.function_5(arguments), indent=4, sort_keys=True)

                elif path_name == "/geneInfo":
                    contents = json.dumps(Us.function_6(arguments), indent=4, sort_keys=True)

                elif path_name == "/geneCalc":
                    contents = json.dumps(Us.function_7(arguments), indent=4, sort_keys=True)

            except KeyError:
                contents = json.dumps(Us.error(), indent=4, sort_keys=True)

            except ValueError:
                contents = json.dumps(Us.error(), indent=4, sort_keys=True)

        else:
            inf_type = "text/html"
            if path_name == "/":
                contents = read_template_html_file("./html/index.html").render()

            elif path_name == "/listSpecies":
                try:
                    if int(arguments["limit"][0]) <= 310 and int(arguments["limit"][0]) >= 0:

                        contents = read_template_html_file("./html/ListSequence.html").render(context=Us.function_1(arguments))

                    elif int(arguments["limit"][0]) >= 310:
                        contents = read_template_html_file("./html/ListSequence.html").render(context=Us.function_2(arguments))

                    else:
                        contents = read_template_html_file("./html/DataError.html").render()

                except KeyError:
                    contents = read_template_html_file("./html/DataError.html").render()

                except ValueError:
                    contents = read_template_html_file("./html/DataError.html").render()


            elif path_name == "/karyotype":
                try:
                    contents = read_template_html_file("./html/Karyotype.html").render(context=Us.function_3(arguments))

                except KeyError:
                    contents = read_template_html_file("./html/DataError.html").render()

            elif path_name == "/chromosomeLength":
                try:
                    contents = read_template_html_file("./html/chromosomeLength.html").render(context=Us.function_4(arguments))

                except KeyError:
                    contents = read_template_html_file("./html/DataError.html").render()

            elif path_name == "/geneSeq":
                try:
                    contents = read_template_html_file("./html/Gene_Seq.html").render(context=Us.function_5(arguments))

                except KeyError:
                    contents = read_template_html_file("./html/DataError.html").render()

            elif path_name == "/geneInfo":
                try:
                    contents = read_template_html_file("./html/Gene_Info.html").render(context=Us.function_6(arguments))

                except KeyError:
                    contents = read_template_html_file("./html/DataError.html").render()


            elif path_name == "/geneCalc":
                try:
                    contents = read_template_html_file("./html/Gene_basis.html").render(context=Us.function_7(arguments))

                except KeyError:
                    contents = read_template_html_file("./html/DataError.html").render()

            else:
                contents = read_template_html_file("./html/Error.html").render()


        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', inf_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))


        return



Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)


    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

