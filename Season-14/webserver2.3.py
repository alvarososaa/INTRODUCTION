import http.server
import socketserver
import termcolor
import pathlib

# Define the Server's port
PORT = 8080
ROOT = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/Season-14/"
ROOT_2 = "/home/alumnos/asosa/PycharmProjects/INTRODUCTION/P4/HTML/ERROR.html"
def read_html_file(FILENAME):
    content = pathlib.Path(FILENAME).read_text()
    return content
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

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        file_name = self.path.strip("/")
        try:
            if file_name == " " or file_name == "index.html":
                contents = read_html_file(ROOT + "index.html")
            else:
                contents = read_html_file(ROOT_2)
        except FileNotFoundError:
            contents = read_html_file(ROOT_2)

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
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