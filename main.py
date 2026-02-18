import http.server

import ngrok


class HelloHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET {self.path}")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from ngrok-python!\n")


def main():
    # Forward ngrok traffic to the local server
    listener = ngrok.forward("localhost:8080", authtoken_from_env=True)
    print(f"Ingress established at: {listener.url()}")

    # Start the HTTP server
    server = http.server.HTTPServer(("localhost", 8080), HelloHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
