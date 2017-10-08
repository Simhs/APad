# -*-coding: utf-8 -*-
from ftplib import FTP

class FTPiot:

    def __init__(self):
        self.sess = None

    def _isLogin(self):
        if self.sess == None:
            return False
        return True

    def login(self,serv_ip,id,passwd):
        if self._isLogin():
            print "기존 로그인 Sess 존재하여 로그아웃을 시도합니다."
            self.logout()
        try:
            print serv_ip,id,passwd,"으로 로그인합니다"
            self.sess = FTP(serv_ip,id,passwd)  # save a line and just put your U:P here.
            return True
        except:
            print "로그인 실패"
            self.sess = None
            return False
    def logout(self):
        if self._isLogin():
            self.sess.close()
        else:
            print "already logouted"

    def ls(self):
        print "서버의 저장공간의 목록을 불러옵니다."
        if self._isLogin():
            return self.sess.nlst()
        else:
            print "로그인이 필요합니다."
            return None

    def upload(self, clientFilePath, outputFileName):
        file = open(clientFilePath, 'rb')
        print self.sess.storbinary('STOR ' + outputFileName, file)
        file.close()

    def download(self,savePath,servFileName):
        fd = open(savePath, 'wb')
        self.sess.retrbinary("RETR " + servFileName, fd.write)
        fd.close()


import datetime
if __name__ == "__main__":
    import time
    ftp = FTPiot()
    ftp.login("192.168.0.90","sim","1234")
    print ftp.ls()
    now = time.localtime()
    s = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    #ftp.upload("./rsc/storage/naruto.mp4","video0.mp4")
    ftp.upload("./rsc/storage/naruto.mp4", s +".mp4")
    #ftp.upload("./rsc/storage/123w.mp4","video0.mp4")
    #ftp.download("./code.py","test.py")


