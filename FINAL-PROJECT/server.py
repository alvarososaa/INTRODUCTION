from urllib.parse import urlparse, parse_qs
import http.server
import socketserver
import termcolor
import http.client
import Server_utils as su
PORT = 8080
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/FINAL-PROJECT/HTML"
SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"
gene_dict = {"FRAT1": "ENSG00000165879",
             "ADA": "ENSG00000196839",
             "FXN": "ENSG00000165060",
             "RNU6_269P": "ENSG00000212379",
             "MIR633": "ENSG00000207552",
             "TTTY4C": "ENSG00000228296",
             "RBMY2YP": "ENSG00000227633",
             "FGFR3": "ENSG00000068078",
             "KDR": "ENSG00000128052",
             "ANK2": "ENSG00000145362"}


socketserver.TCPServer.allow_reuse_address = True

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
        print("Resoruce requested: ", path_name)
        print("Parameters: ", arguments)
        if path_name == "/":
            context = {"gene_list": gene_dict}
            contents = su.read_template_html_file(ROOT + "/Basic_level.html").render(context=context)
        elif path_name == "/listSpecies":
            ENDPOINT = "/info/species"
            response = su.api_connection(ENDPOINT, PARAMS, SERVER)
            try:
                if type(arguments["limit"][0]) == str:
                    contents = su.species_list(response, int(arguments["limit"][0]))
            except KeyError:
                contents = su.species_list(response)
        elif path_name == "/Karyotype":
            try:
                ENDPOINT = "/info/assembly/"
                specie = arguments["specie"][0]
                ENDPOINT = ENDPOINT + specie
                response = su.api_connection(ENDPOINT, PARAMS, SERVER)
                context = {"specie": specie,
                           "karyotype": response["karyotype"]}
                contents = su.read_template_html_file(ROOT + "/karyotype.html").render(context=context)
            except KeyError:
                contents = su.read_template_html_file(ROOT + "/ERROR.html").render()
        elif path_name == "/chromosomeLength":
            try:
                ENDPOINT = "/info/assembly/"
                specie = arguments["specie"][0]
                chromo = arguments["chromo"][0]
                ENDPOINT = ENDPOINT + specie
                response = su.api_connection(ENDPOINT, PARAMS, SERVER)
                contents = su.chromosome_length(response, specie, chromo)
            except KeyError:
                contents = su.read_template_html_file(ROOT + "/ERROR.html").render()
        elif path_name == "/geneSeq":
            ENDPOINT = "/sequence/id/"
            ID = arguments["gene"][0]
            ENDPOINT = ENDPOINT + gene_dict[ID]
            response = su.api_connection(ENDPOINT, PARAMS, SERVER)
            context ={"Sequence": response["seq"],
                      "name": ID,
                      "id": response["id"]}
            contents = su.read_template_html_file(ROOT + "/GENE.html").render(context=context)
        elif path_name == "/geneInfo":
            ENDPOINT = "/sequence/id/"
            ID = arguments["gene"][0]
            ENDPOINT = ENDPOINT + gene_dict[ID]
            response = su.api_connection(ENDPOINT, PARAMS, SERVER)
            contents = su.calculations(response, ID)
        elif path_name == "/geneCalc":
            ENDPOINT = "/sequence/id/"
            ID = arguments["gene"][0]
            ENDPOINT = ENDPOINT + gene_dict[ID]
            response = su.api_connection(ENDPOINT, PARAMS, SERVER)
            contents = su.second_calculations(response, ID)



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