import http.server
import socketserver
import termcolor
import pathlib
import json

# Define the Server's port
PORT = 8081
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P5/HTML"
def read_html_file(FILENAME):
    content = pathlib.Path(FILENAME).read_text()
    return content
answer = {'Name': 'Adenine', 'Letter' : 'A' ,
'Link': 'https://en.wikipedia.org/wiki/Adenine', 'Formula': 'C5H5N5'}
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

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file(ROOT + "/index.html")
        elif self.path == "/info/A":
            contents = json.dumps(answer, indent=4, sort_keys=True)
        elif self.path == "/info/C":
            contents = read_html_file(ROOT + "/INFO/C.html")
        elif self.path == "/info/G":
            contents = read_html_file(ROOT + "/INFO/G.html")
        elif self.path == "/info/T":
            contents = read_html_file(ROOT + "/INFO/T.html")
        elif self.path.endswith(".html"):
            try:
                contents = read_html_file(ROOT + self.path.split(".")[0])
                print(self.path.split(".")[0])
            except FileNotFoundError:
                contents = read_html_file(ROOT + "/ERROR.html")

        else:
            contents = read_html_file(ROOT + "/ERROR.html")


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