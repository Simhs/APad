# -*-coding: utf-8 -*-
'''
    udp socket client
    Silver Moon
'''

import socket  # for sockets
import sys  # for exit

# create dgram udp socket
class MSGclient:
    def __init__(self,host,port):
        self.host = host;
        self.port = port
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
    def send(self,string):

        msg = string
        try:
            self.s.sendto(msg, (self.host, self.port))
            d = self.s.recvfrom(1024)
            reply = d[0]
            if reply == "OK":
                self.s.close()
                return True
            else:
                self.s.close()
                return False
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            self.s.close()
            return False
    def close(self):
        self.s.close()

from FTP4iot import  FTPiot
import time
if __name__=="__main__":
    ftp = FTPiot()
    if not ftp.login("192.168.0.90","sim","1234"):
        #tkMessageBox.showinfo("login failed", "Please check you id,password or Apad's IP")
        print"z"
    now = time.localtime()
    s = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    ftp.upload("./rsc/mode/"+ "keyboard.play", s + ".play")
    client = MSGclient("192.168.0.90",5000)
    print "?"
    while True:
        print "!"
        if not client.send("dd"):
            print "err"
        print "?"
