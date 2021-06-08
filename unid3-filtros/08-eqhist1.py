from cv2 import *
import numpy as np

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

IMG1 = total_path + 'moonsurface.png'
IMG2 = total_path + 'QuadradosColoridos.png'

BANDA_Y  = 0
BANDA_Cb = 2
BANDA_Cr = 1

W_NAME_ORI  = 'Original'
W_NAME_GRAY = 'Niveis de Cinza'
W_NAME_Y    = 'Canal Y'
W_NAME_Cb   = 'Canal Cb'
W_NAME_Cr   = 'Canal Cr'
W_NAME_YEQ  = 'Canal Y Eq'
W_NAME_RES  = 'Resultante'


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

# Equalizar a banda Y
aux = 255*imgY
imgY = equalizeHist(aux.astype(np.uint8))

imshow(W_NAME_YEQ, imgY)
waitKey(0)

imgYCbCr[:,:,BANDA_Y] = imgY.astype(float)/255
imgRGBf = cvtColor(imgYCbCr, COLOR_YCrCb2BGR)
imshow(W_NAME_RES,  imgRGBf)
waitKey(0)


