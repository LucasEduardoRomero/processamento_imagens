# HSI eh igual a HSL ou, no OpenCV, HLS
from cv2 import *
import numpy as np

IMG1 = 'lenna.jpg'
IMG2 = 'QuadradosColoridos.png'

BANDA_Y  = 0
BANDA_Cb = 2
BANDA_Cr = 1

W_NAME_ORI  = 'Original'
W_NAME_GRAY = 'Niveis de Cinza'
W_NAME_Y    = 'Canal Y'
W_NAME_Cb   = 'Canal Cb'
W_NAME_Cr   = 'Canal Cr'


img1 = imread(IMG1)
(w, h, c) = img1.shape
imgRGBf = np.zeros((w,h,3), dtype=np.float32)
imgRGBf += img1/255.0

imgGray = cvtColor(imgRGBf, COLOR_RGB2GRAY)

imshow(W_NAME_ORI, img1)
imshow(W_NAME_GRAY, imgGray)


imgYCbCr = cvtColor(imgRGBf, COLOR_BGR2YCrCb)
imgY   = imgYCbCr[:,:,BANDA_Y]
imgCb  = imgYCbCr[:,:,BANDA_Cb]
imgCr  = imgYCbCr[:,:,BANDA_Cr]

imshow(W_NAME_Y,  imgY)
imshow(W_NAME_Cb, imgCb)
imshow(W_NAME_Cr, imgCr)

waitKey(0)

