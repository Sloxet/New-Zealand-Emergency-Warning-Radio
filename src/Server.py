try:
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

import sys
import os

if sys.argv[1:]:
    address = sys.argv[1]
    if (':' in address):
        interface, port = address.split(':')
    else:
        interface, port = '0.0.0.0', int(address)
else:
    port, interface = 8000, '0.0.0.0'

if sys.argv[2:]:
    os.chdir(sys.argv[2])

server = ThreadingSimpleServer((interface, port), SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print('Finished.')