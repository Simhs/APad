#-*- coding: utf-8 -*-


from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import ttk
import os
import tkMessageBox
from imageconverter import *
from commandclient import MSGclient
from FTP4iot import FTPiot
import time
from pynput import keyboard

import thread

class Gui:
    def __init__(self, master,controlObject):

        self.CONVERTED_STORAGE_PATH = "./rsc/storage/"
        self.KEYBOARD_EFFECT_PATH = "./rsc/mode/"
        self.BACKGROUND_IMAGE_PATH = "./rsc/image/bg.png"
        self.NETWORK_CONFIG_FILE_PATH = "./rsc/config/network.conf"

        self.master = master
        master.title("APad")
        self.w = Label(master)
        self.w.configure(background='black')
        self.disconnectedimg = ImageTk.PhotoImage(Image.open(self.BACKGROUND_IMAGE_PATH))
        self.w.image = self.disconnectedimg
        self.w.configure(image=self.disconnectedimg)

        self.w.grid(row=0, column=0, columnspan=3,  sticky=W + E + N + S)

        self.label1 = Label(master, text="IP   :")
        self.label2 = Label(master, text="ID:")
        self.label3 = Label(master, text="passwd:")
        self.label1.grid(row=1, column=0)
        self.label2.grid(row=2, column=0)
        self.label3.grid(row=3, column=0)

        self.entry1 = Entry(master, text="a")
        self.entry2 = Entry(master, text="b")
        self.entry3 = Entry(master, text="c")
        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)
        self.entry3.grid(row=3, column=1)

        self.var1 = IntVar()
        self.checkBox1 = Checkbutton(master, text="remember IP and Port", variable=self.var1)
        self.var1.set(1)
        self.checkBox1.grid(row=4, column=0,columnspan=2)

        self.RlabelSearch = Label(master, text="사진&동영상 변환")
        self.RlabelSearch.grid(row=5, column=0, columnspan=1, sticky=W)
        self.fileNameEntry1 = Entry(master, text="d")
        self.fileNameEntry1.grid(row=5, column=1,columnspan=1,sticky=W)
        self.filepickerBt1 = Button(master, text="search", command=lambda: self.searchImage())
        self.filepickerBt1.grid(row=5, column=2,sticky=E)

        self.trbt = Button(master, text="변환하기", command=lambda: self.convertFile())
        self.trbt.grid(row=6, column=0, columnspan=3)

        self.countryvar = StringVar()
        self.country = ttk.Combobox(master, textvariable=self.countryvar)
        self.country.grid(row=7, column=0,columnspan=2, sticky=W+E)
        self.updateListbt = Button(master, text="Send to APad", command=lambda: self.button(0))
        self.updateListbt.grid(row=7, column=2,sticky=E)
        self.country['values'] = os.listdir(self.CONVERTED_STORAGE_PATH)

        self.pb_send = ttk.Progressbar(master, orient='horizontal', mode='determinate',length=100)
        self.pb_send.grid(row=8, column=0,columnspan=3, sticky=W+E)
        self.pb_send['value']=40

        self.bt1 = Button(master, text="Combo Stop ", command=lambda: self.keyEffectstopButton())#, command=lambda: self.button(0))
        self.bt1.grid(row=9, column=1, columnspan=2,sticky=E)

        self.bt2 = Button(master, text="Combo Start", command=lambda: self.keyEffectstartButton())
        self.bt2.grid(row=9, column=0, columnspan=2,sticky=W)

        try:
            f = open(self.NETWORK_CONFIG_FILE_PATH, "r")
            self.entry1.insert(END, str(f.readline()[:-1]))
            self.entry2.insert(END, str(f.readline()[:-1]))
            self.entry3.insert(END, str(f.readline()))
            f.close()
        except:
            pass
        finally:
            pass
        self.lis = None



    def listReflush(self):
        print "reflushed"
        #print os.listdir(self.STORAGE_PATH)
        self.country['values'] = os.listdir(self.CONVERTED_STORAGE_PATH)


    def searchImage(self):
        self.fileNameEntry1.delete(0, 'end')
        file_path_string = tkFileDialog.askopenfilename()
        self.fileNameEntry1.insert(END, file_path_string)

    def convertFile(self):
        filePath = self.fileNameEntry1.get()
        ic = ImageConverter()
        ic.imwrite(filePath, self.CONVERTED_STORAGE_PATH)
        self.listReflush()
        self.fileNameEntry1.delete(0, 'end')

    def updateThread(self):
        self.master.after(200, self.updateThread)

    def on_press(self,key):
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print k
        client = MSGclient(self.entry1.get(), 5000)
        client.send("key")

    def keyEffectstartButton(self):

        ftp = FTPiot()
        if not ftp.login(self.entry1.get(), self.entry2.get(), self.entry3.get()):
            tkMessageBox.showinfo("login failed", "Please check you id,password or Apad's IP")
            return
        now = time.localtime()
        s = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        ftp.upload(self.KEYBOARD_EFFECT_PATH + "greenrain.mp4", "greenrain.mp4")
        self.lis = keyboard.Listener(on_press=self.on_press)
        self.lis.start()  # start to listen on a separate thread
        client = MSGclient(self.entry1.get(), 5000)
        client.send("start")

    def keyEffectstopButton(self):
        client = MSGclient(self.entry1.get(), 5000)
        client.send("end")
        print "end send"
        self.lis.stop()
        self.lis.join()
        self.lis = None

    def button(self,argv):
        ftp = FTPiot()
        if not ftp.login(self.entry1.get(), self.entry2.get(), self.entry3.get()):
            tkMessageBox.showinfo("login failed", "Please check you id,password or Apad's IP")
            return

        now = time.localtime()
        s = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        self.country['values'] = os.listdir(self.CONVERTED_STORAGE_PATH)
        fileName = self.countryvar.get()
        if "" == fileName:
            tkMessageBox.showinfo("combobox exception", "Please, Select imageFile or videoFile")
            ftp.logout()
            return
        fname, ext = os.path.splitext(fileName)
        print self.CONVERTED_STORAGE_PATH+fileName, s + ext
        ftp.upload(self.CONVERTED_STORAGE_PATH+fileName, s + ext)
        time.sleep(2)

    def close(self):
        print("종료!!")
        if self.var1.get() == 1:
            f = open(self.NETWORK_CONFIG_FILE_PATH,"w")
            f.write(self.entry1.get())
            f.write("\n")
            f.write(self.entry2.get())
            f.write("\n")
            f.write(self.entry3.get())
            f.close()
        else:
            f = open(self.NETWORK_CONFIG_FILE_PATH, "w")
            f.close()
        self.master.destroy()


if __name__=="__main__":
    root = Tk()
    gui = Gui(root,None)
    root.mainloop()