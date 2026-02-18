import http.server
import threading

import ngrok


def main():
    # Start a simple HTTP server
    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(("localhost", 8080), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    # Forward ngrok traffic to the local server
    listener = ngrok.forward("localhost:8080", authtoken_from_env=True)
    print(f"Ingress established at: {listener.url()}")

    # Keep the process running
    input("Press Enter to exit...\n")


if __name__ == "__main__":
    main()
