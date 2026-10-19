#!/usr/bin/env python3
"""
SkillConnect - Local Job & Skill Matching Portal
Lightweight Python HTTP Server supporting clean URL routing:
  /         -> index.html
  /jobs     -> jobs.html
  /workers  -> workers.html
  /login    -> login.html
  /signup   -> signup.html
  /about    -> about.html
"""

import http.server
import socketserver
import os
import sys
import urllib.parse

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

ROUTE_MAP = {
    '/': 'index.html',
    '/jobs': 'jobs.html',
    '/workers': 'workers.html',
    '/login': 'login.html',
    '/signup': 'signup.html',
    '/about': 'about.html',
}

class SkillConnectHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        clean_path = parsed.path.rstrip('/')
        if not clean_path:
            clean_path = '/'

        # Check clean routing map
        if clean_path in ROUTE_MAP:
            target_file = ROUTE_MAP[clean_path]
            file_path = os.path.join(DIRECTORY, target_file)
            if os.path.isfile(file_path):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
                return

        # Fallback to standard static file serving
        return super().do_GET()

def run():
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass

    handler = SkillConnectHTTPRequestHandler
    
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print("=" * 65)
            print("🚀 SkillConnect Portal Server Running!")
            print("=" * 65)
            print(f"• Local URL:      http://localhost:{port}/")
            print(f"• Find Jobs:      http://localhost:{port}/jobs")
            print(f"• Find Workers:   http://localhost:{port}/workers")
            print(f"• Login Page:     http://localhost:{port}/login")
            print(f"• Sign Up Page:   http://localhost:{port}/signup")
            print(f"• About Page:     http://localhost:{port}/about")
            print("=" * 65)
            print("Press Ctrl+C to stop the server.")
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e) or e.errno == 98 or e.errno == 10048:
            port = port + 1
            print(f"Port was busy, switching to http://localhost:{port}/")
            with socketserver.TCPServer(("", port), handler) as httpd:
                httpd.serve_forever()
        else:
            raise

if __name__ == '__main__':
    run()
