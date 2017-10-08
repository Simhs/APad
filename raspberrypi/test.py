import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix
import cv2
import time


matrix = Adafruit_RGBmatrix(32, 2)
cap = cv2.VideoCapture('./FTPDownload/video.mp4')
total_frame = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
count = 1
while(True):
    _,frame=cap.read()
    cv2.waitKey(24)
    pil_im=Image.fromarray(frame)
    matrix.SetImage(pil_im.im.id, 0, 0)
    count +=1
    if count >= total_frame - 1:
        cap.set(1,1)
        count = 1
matrix.Clear()
cap.release()
# Rows and chain length are both required parameters:
 
# Bitmap example w/graphics prims
# Draw some shapes into image (no immediate effect on matrix)...
# Then scroll image across matrix...
# 8-bit paletted GIF scrolling example
#

