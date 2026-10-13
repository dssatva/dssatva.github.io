#!/usr/bin/env python3
"""DS Satva dev server — same as `python3 -m http.server`, but tells the browser
never to cache. Without this, edits to css/satva.css and js/satva.js keep being
served from the browser's cache and every change needs a manual hard refresh."""
import http.server, socketserver, os

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()
    def log_message(self, *a):
        pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 8002), NoCache) as httpd:
    httpd.serve_forever()
