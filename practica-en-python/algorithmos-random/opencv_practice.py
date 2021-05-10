import cv2 as cv
import numpy as np
path = "C:\\Users\\asus 2020\\Desktop\\LITO-CLASES\\python-command-terminal-stuff\\practica-en-python\\algorithmos-random\\FOTOS Y VIDEOS BRI 0-3 meses"
img = cv.imread(path+"\\bumpie_week_27_flag.jpg",0)
cols, rows = img.shape
for a in range(1,20):
    M = np.float32([np.random.randn(3,1),np.random.randn(3,1)])
    M2 = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    print(M)
    dst = cv.warpAffine(img,M,(cols,rows))
    dst2 = cv.warpAffine(dst,M2,(cols,rows)) 
    cv.imshow("img",dst2)
    cv.waitKey(0)
    cv.destroyAllWindows()
