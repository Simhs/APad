# -*- coding: utf-8 -*-
'''
    Simple udp socket server
'''

import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5000  # Arbitrary non-privileged port

class MSGserver:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.s = None
    def listen(self):
        # Datagram (udp) socket
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print 'Socket created'
        except socket.error, msg:
            print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

        # Bind socket to local host and port
        try:
            self.s.bind((HOST, PORT))
        except socket.error, msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        print 'Socket bind complete'
    def recv(self):
        # now keep talking with the client
        # receive data from client (data, addr)
        d = self.s.recvfrom(1024)
        data = d[0]
        addr = d[1]
        #addr = int(addr)
        #print "addr",addr

        if not data:
            return "err"
        self.s.sendto('OK',addr)
        return data.strip()
    def close(self):
        self.s.close()

if __name__=="__main__":
    serv = MSGserver("localhost",5000)
    serv.listen()
    count = 0
    while True:
        count +=1
        if not serv.recv():
            print "err"
        if count == 19:
            serv.close()
            break


