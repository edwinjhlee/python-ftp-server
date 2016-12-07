from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import sys

import os
env = os.environ

STORAGE_PATH = "/tmp/storage"

def setupHandler():
    authorizer = DummyAuthorizer()

    if "FTP_USERS" in env:
        userlist = env["FTP_USERS"].split(',')
        passwordlist = env["FTP_PASSWORDS"].split(',')
        for u, p in zip(userlist, passwordlist):
            authorizer.add_user(u, p, STORAGE_PATH, perm='elradfmwM')

        if "ENABLE_FTP_ENORMOUS" in env:
            authorizer.add_anonymous(STORAGE_PATH, perm='elr')
    else:
        print "annoymous login enable with full access"
        print "What"
        authorizer.add_anonymous(STORAGE_PATH, perm='elradfmwM')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = env["BANNER"] if "BANNER" in env else "FTP Server"
    return handler

def enablePassiveMode(handler, masquerade_address):
    handler.masquerade_address = masquerade_address
    handler.passive_ports = range(65000, 65536)

def setupServer(handler):
    address = ('', 21)

    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

def main():
    handler = setupHandler()
    
    if len(sys.argv) >= 2:
        print "Using masquerade_address", sys.argv[1]
        enablePassiveMode(handler, sys.argv[1])

    setupServer(handler)    

if __name__ == '__main__':
    main()