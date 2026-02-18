import http.server

import ngrok


class HelloHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET {self.path}")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from ngrok-python!\n")


server = http.server.HTTPServer(("localhost", 0), HelloHandler)
ngrok.listen(server)
print(f"Ingress established at: {server.url}")
server.serve_forever()
