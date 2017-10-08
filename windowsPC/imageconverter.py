import cv2
import os
class ImageConverter:
    def __init__(self):
        pass
    def imwrite(self,filePath,outputPath):
        if self.checkExtension(filePath, "png"):
            pass
        elif self.checkExtension(filePath, "jpg"):
            pass
        elif self.checkExtension(filePath, "mp4") or self.checkExtension(filePath, "avi"):
            fourcc1 = cv2.VideoWriter_fourcc(*'DIVX') # window codec
            fileName = os.path.basename(filePath)
            out = cv2.VideoWriter( outputPath+fileName, fourcc1, 24.0, (64, 32))
            cap = cv2.VideoCapture(filePath)
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    crop = self.cropFrom2t1Rate(frame)
                    resized = self.resize64x32(crop)
                    BGR = cv2.cvtColor(resized,cv2.COLOR_RGB2BGR)
                    out.write(BGR)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            # Release everything if job is finished
            cap.release()
            out.release()

    def checkExtension(self, filename, extension):
        file_len = len(filename)
        ext_len = len(extension) + 1
        if str.upper(filename[file_len - ext_len:]) == "." + str.upper(extension):
            return True
        else:
            return False
    def cropFrom2t1Rate(self,img):
        h = img.shape[0]
        w = img.shape[1]
        crop_h = 1
        crop_w = 2
        while True:
            findout = [False, False]
            if w >= crop_w:
                findout[0] = True
            if h >= crop_h:
                findout[1] = True
            if findout[0] and findout[1]:
                crop_h += 1
                crop_w += 2
            else:
                crop_h -= 1
                crop_w -= 2
                crop_img = img[int((h - crop_h) / 2.0): int((h - crop_h) / 2.0) + crop_h,
                           int((w - crop_w) / 2.0): int((w - crop_w) / 2.0) + crop_w]
                return crop_img

    def resize64x32(self,img):
        resized = cv2.resize(img, (64, 32), interpolation=cv2.INTER_CUBIC)
        return resized

if __name__ == "__main__":
    pass
