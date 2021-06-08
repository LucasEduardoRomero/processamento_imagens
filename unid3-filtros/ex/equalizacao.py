from cv2 import *
import numpy as np

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

IMG = total_path + 'lenna.jpg'

BANDA_R = 2
BANDA_G = 1
BANDA_B = 0

W_NAME_ORI  = 'Original'
W_NAME_RES  = 'Resultante'


img = imread(IMG)
(w, h, c) = img.shape

imshow(W_NAME_ORI, img)

# Equalizar as bandas
imgR = equalizeHist(img[:,:,BANDA_R])
imgG = equalizeHist(img[:,:,BANDA_G])
imgB = equalizeHist(img[:,:,BANDA_B])

res = img.copy()
res[:,:,BANDA_R] = imgR
res[:,:,BANDA_G] = imgG
res[:,:,BANDA_B] = imgB

imshow(W_NAME_RES, res)
waitKey(0)