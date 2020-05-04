#!/usr/bin/env python
import time
from constants import *
from os.path import join, dirname
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        else:
            self.path = '/' + self.path + '.html'

        try:
            file_path = './' + VIEWS_DIR + self.path
            file_to_open = open(file_path).read()
            self.send_response(200)
        except:
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((HOST, PORT), Server)
    print("Server started http://%s:%s" % (HOST, PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
