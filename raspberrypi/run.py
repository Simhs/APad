#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import cv2
import thread
from commandserv import MSGserver
import Image
from rgbmatrix import Adafruit_RGBmatrix
import time
from matrixnumberfont import Font 
DOWNLOAD_DIR ="/home/pi/Desktop/APad/FTPDownload/"
#DOWNLOAD_DIR ="./FTPDownload/"
time.sleep(4)

first_video_name = os.listdir(DOWNLOAD_DIR)
playFileName = ""
for name in first_video_name:
    playFileName = DOWNLOAD_DIR+name
    break



class RGBMatrixDisplay:
    def __init__(self):
        self.curFileName = ""
        self.matrix = None
        self.alloc_matrix()
        self.font = Font()
        self.font.setColor(1,255,1)
        self.num = 0        
        thread.start_new_thread(self.keythread,())
    def alloc_matrix(self):
        self.matrix = Adafruit_RGBmatrix(32, 2)

    def free_matrix(self):
        self.matrix.Clear()
        self.matrix = None

    def checkExtension(self, filename, extension):
        
        file_len = len(filename)
        ext_len = len(extension) + 1
        if str.upper(filename[file_len - ext_len:]) == "." + str.upper(extension):
            return True
        else:
            return False
        '''
        fname,ext = os.path.splitext(filename)
        if ext == extension:
            return True
        else:
            return False

        '''
    
    def keythread(self):
        serv = MSGserver("localhost", 5000)
        serv.listen()
        self.num = 0
        while True:
            data = serv.recv()
            if data == "start":
                self.num = 1
            elif data == "key":
                self.num +=1
            elif data == "end":
                self.num = 0
            elif data == "err":
                sys.exit()
            
    
    def show(self):
        global playFileName
        self.curFileName = playFileName
        while True:
            if self.checkExtension(self.curFileName,"mp4") or self.checkExtension(self.curFileName,"avi"):
                cap = cv2.VideoCapture(self.curFileName)
                total_frame = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
                count = 1
                while (True):
                    #time.sleep(1)
                    if self.curFileName != playFileName:
                        self.curFileName = str(playFileName)
                        print "현재 파일1 :", self.curFileName
                        print "break video loop"
                        break

                    _, frame = cap.read()
                    cv2.waitKey(24)
                    pil_im = Image.fromarray(frame)
                    self.matrix.SetImage(pil_im.im.id, 0, 0)
                    combo = self.num

                    if combo >0:
                        s = str(combo)
                        sl = len(s)
                        x_start_pos =32-int((sl*6)/2.0)
                        for index,n in enumerate(s):
                            self.font.drawNumber(self.matrix,x_start_pos+(index*6),13,int(n))
                    else:
                        pass
                    #print "state: playing the video" ,self.curFileName ,playFileName
                    count += 1
                    if count >= total_frame - 1:
                        cap.set(1, 1)
                        count = 1
                cap.release()
                print "releaesed video"
            '''
            elif self.checkExtension(self.curFileName,"play"):
                serv = MSGserver("localhost", 5000)
                serv.listen()
                num = 0
                while True:
                    print "loop start"
                    if self.curFileName != playFileName:
                        print "cur : ",self.curFileName 
                        print "glo : ",playFileName
                        self.curFileName = str(playFileName)
                        print "loop break and sock close"
                        serv.close()
                        break

                    print serv.recv()
                    print num
                    #for index,nu in enumerate(str(num)):
                    #    font.drawNumberFont(matrix,32+index*6,12,int(nu))
                    num +=1
            '''



class MyHandler(FTPHandler):
    def on_file_received(self, file):
        global playFileName
        dirlist = os.listdir(DOWNLOAD_DIR)
        downloadFile = os.path.basename(file)
        for i in dirlist:
            if i == downloadFile:
                pass
            else:
                print DOWNLOAD_DIR+i
                os.remove(DOWNLOAD_DIR+i)
        print "now FTPDownload folder state :",os.listdir(DOWNLOAD_DIR)
        print "@@@@@@@@@@@@@@@@@@@@"
        playFileName = file
        print "####################"
        

authorizer = DummyAuthorizer()
authorizer.add_user("sim", "1234", DOWNLOAD_DIR, perm="elradfmw")

handler = MyHandler
handler.passive_ports = range(60000, 65535)
handler.authorizer = authorizer
server = FTPServer(("", 21), handler)

display = RGBMatrixDisplay()
thread.start_new_thread(display.show,())
server.serve_forever()
