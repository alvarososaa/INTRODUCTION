from urllib.parse import urlparse, parse_qs
import http.server
import socketserver
import termcolor
import server_utils as su

# Define the Server's port
PORT = 8081
INFORMATION = {"A": {"LINK":"https://es.wikipedia.org/wiki/Adenina" , "formula": "C5H5N5", "name": "ADENINE", "color" : "blue"},
               "T": {"LINK":"https://es.wikipedia.org/wiki/Timina" , "formula": "C5H6N202", "name": "THYMINE", "color": "pink"},
               "G": {"LINK":"https://es.wikipedia.org/wiki/Guanina" , "formula": "C5H5N50", "name": "GUANINE", "color": "lightblue"},
               "C": {"LINK":"https://es.wikipedia.org/wiki/Citosina" , "formula": "C4H5N30", "name": "CYTOSINE", "color": "yellow"}}
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P6/HTML"
LIST_SEQUENCES = ["ACACACACACACACA" , "ATATATATATAT" , "AGAGCGAGCGAGT" , "ATATATCTGT" , "AAAA"]
ROOT_GENE = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P6/SEQUENCES/"
GENE_LIST = ["ADA" , "FRAT1", "FXN" , "RNU6_269P", "U5"]
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
        termcolor.cprint(self.path, "blue")
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("PATH NAME: ", path_name)
        print("Arguments: ", arguments)

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        context = {}
        if path_name == "/":
            context = {"n_sequences": len(LIST_SEQUENCES),
                       "gene_list": GENE_LIST}
            contents = su.read_template_html_file(ROOT + "/Main_form.html").render(context=context)
        elif path_name == "/ping":
            contents = su.read_template_html_file(ROOT + "/ping_ok.html").render()
        elif path_name == "/get":
            contents = su.get(LIST_SEQUENCES, int(arguments["sequence"][0]))
        elif path_name == "/gen":
            contents = su.gen(arguments["gene"][0])



        else:
            contents = su.read_template_html_file(ROOT + "/ERROR.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))

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