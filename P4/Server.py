import socket
from pathlib import Path

import termcolor

# from urllib.parse import urlparse, parse_qs --> only works with HTTP protocols

HTML_ASSETS = "./html/"

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

def read_html_file(filename):
    contents = Path(filename).read_text()
    return contents

def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line with the path is the first
    req_line = lines[0]
    request = req_line.split(" ")[1]

    path_name = request.split("?")[0]

    try:
        parameters = request.split("?")[1]
        print("Arguments", parameters)
    except IndexError:
        pass

    print("Resource requested: ", path_name)
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    body = read_html_file(HTML_ASSETS + "menu.html")

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    if path_name == "/":
        body = read_html_file(HTML_ASSETS + "menu.html")
    elif "/info/" in path_name:
        try:
            body = read_html_file(HTML_ASSETS + path_name.split("/")[-1] + ".html")
        except FileNotFoundError:
            body = read_html_file(HTML_ASSETS + "error.html")
    else:
        body = read_html_file(HTML_ASSETS + "error.html")

    header += f"Content-Length: {len(body)}\n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        # Service the client
        process_client(cs)
        # -- Close the socket
        cs.close()
