#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)

            self.send_header("Content-type", "text/html")
            self.end_headers()

            message = f"Hello, this is a simple API!"
            self.wfile.write(bytes(message, "utf8"))

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            
            self.send_header("Content-type", "application/json")
            self.end_headers()

            message = f"{data}"
            self.wfile.write(json.dumps(data).encode("utf8"))

        elif self.path == "/status":
            self.send_response(200)
            
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            message = "OK"
            self.wfile.write(bytes(message, "utf8"))

        else:
            self.send_response(404)

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            message = f"Page not found"
            self.wfile.write(bytes(message, 'utf8'))


def run_server():

    PORT = 8000

    Handler = MyRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        print("serving at port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()


if __name__ == "__main__":
    
    run_server()