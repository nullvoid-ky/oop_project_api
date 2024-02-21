# simple_web_server.py

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        elif self.path == '/second_page':
            self.path = 'second_page.html'
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    PORT = 8000
    Handler = CustomHandler

    with TCPServer(("localhost", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
