#!/usr/bin/env python

"""Simple HTTP server for Robot Framework web testing.

Usage:  server.py [port]

This server serves HTML pages under `html` directory. Server is started simply
by running this script from the command line. In the former case the server can 
be shut down with Ctrl-C.

*in terminal run $python roboCop/server.py

"""

from os import chdir
from os.path import abspath, dirname, join
from SocketServer import TCPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


ROOT = join(dirname(abspath(__file__)), 'html')
PORT = 7272


class DemoServer(TCPServer):
    allow_reuse_address = True

    def __init__(self, port=PORT):
        TCPServer.__init__(self, ('localhost', int(port )), SimpleHTTPRequestHandler)

    def serve(self, directory=ROOT):
        chdir(directory)
        print 'Demo server starting on port %d.' % self.server_address[1]
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()
        print 'Demo server stopped.'


if __name__ == '__main__':
    import sys
    try:
        server = DemoServer(*sys.argv[1:])
    except (TypeError, ValueError):
        print __doc__
    else:
        server.serve()