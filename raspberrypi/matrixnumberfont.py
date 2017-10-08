#!/usr/bin/python

# Simple RGBMatrix example, using only Clear(), Fill() and SetPixel().
# These functions have an immediate effect on the display; no special
# refresh operation needed.
# Requires rgbmatrix.so present in the same directory.

import time
from rgbmatrix import Adafruit_RGBmatrix




class Font:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

    def setColor(self,r,g,b):
        self.r = int(r)#/16.0)
        self.g = int(g)#16.0)
        self.b = int(b)#16.0)
    def drawNumber(self,matrix,x,y,num):
        if num == 0:
            # zero
            matrix.SetPixel(x+1,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y  ,self.r,self.g,self.b)

            matrix.SetPixel(x  ,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x  ,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x  ,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x  ,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x  ,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
            
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)
        elif num == 1:
            #one
            matrix.SetPixel(x+2,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)
        elif num ==2:
            #two
            matrix.SetPixel(x+1,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x  ,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+6,self.r,self.g,self.b)

        elif num == 3:
            #three
            matrix.SetPixel(x+1,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y  ,self.r,self.g,self.b)
            matrix.SetPixel(x  ,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+2,self.r,self.g,self.b)
            
            matrix.SetPixel(x+1,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+3,self.r,self.g,self.b)
           

            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
 
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)

        elif num ==4:

            matrix.SetPixel(x+3,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+1,self.r,self.g,self.b)

            matrix.SetPixel(x+1,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+2,self.r,self.g,self.b)
            
            matrix.SetPixel(x+1,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)
        
            
            matrix.SetPixel(x+0,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+4,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)

            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)

        elif num ==5:
            # five
            
            matrix.SetPixel(x+1,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)
            
            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)
        elif num == 6:
            #six
            matrix.SetPixel(x+1,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+0,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)
             
            matrix.SetPixel(x+0,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)
        elif num == 7:
            #seven 
            matrix.SetPixel(x+1,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+6,self.r,self.g,self.b)
        elif num == 8:
            matrix.SetPixel(x+1,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+0,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+1,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+2,self.r,self.g,self.b)
            
            matrix.SetPixel(x+1,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
            
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)


        elif num == 9:
            matrix.SetPixel(x+1,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+0,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+0,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+1,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+1,self.r,self.g,self.b)

            matrix.SetPixel(x+0,y+2,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+2,self.r,self.g,self.b)
            
            matrix.SetPixel(x+1,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+3,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+3,self.r,self.g,self.b)

            matrix.SetPixel(x+4,y+4,self.r,self.g,self.b)
            matrix.SetPixel(x+0,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+4,y+5,self.r,self.g,self.b)
            matrix.SetPixel(x+1,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+2,y+6,self.r,self.g,self.b)
            matrix.SetPixel(x+3,y+6,self.r,self.g,self.b)


if __name__=="__main__":

    matrix = Adafruit_RGBmatrix(32, 2)

    font = Font()
    font.setColor(1,255,1)
    for i in range(10):
        for w in range(64):

            font.drawNumber(matrix,w,0,i)
            time.sleep(0.02)
            matrix.Fill(0x000000)
    matrix.Clear()
