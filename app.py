import os
from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = open("index.html", "rb").read()

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(HTML)

port = int(os.environ.get("PORT", 8080))
print(f"Running on port {port}")
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
