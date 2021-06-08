# HSI eh igual a HSL ou, no OpenCV, HLS
from cv2 import *
import numpy as np

IMG1 = 'lenna.jpg'
IMG2 = 'QuadradosColoridos.png'

BANDA_H = 0
BANDA_L = 1
BANDA_S = 2

W_NAME_ORI  = 'Original'
W_NAME_GRAY = 'Niveis de Cinza'
W_NAME_H    = 'Canal H'
W_NAME_S    = 'Canal S'
W_NAME_L    = 'Canal L'


img1 = imread(IMG1)
(w, h, c) = img1.shape
imgRGBf = np.zeros((w,h,3), dtype=np.float32)
imgRGBf += img1/255.0

imgGray = cvtColor(imgRGBf, COLOR_RGB2GRAY)

imshow(W_NAME_ORI, img1)
imshow(W_NAME_GRAY, imgGray)


imgHLS = cvtColor(imgRGBf, COLOR_BGR2HLS)
imgH   = imgHLS[:,:,BANDA_H]
imgL   = imgHLS[:,:,BANDA_L]
imgS   = imgHLS[:,:,BANDA_S]

###################################
# Rotacao 180 graus para perceber melhor
# as variacoes do H na imagem
imgH += 180
aux = (imgH > 360)
imgH = imgH - aux*360
###################################
imgH = imgH/360.0	 # converter H para o intervalo [0, 1]

imshow(W_NAME_H, imgH)
imshow(W_NAME_S, imgS)
imshow(W_NAME_L, imgL)

waitKey(0)

