from cv2 import *
import numpy as np
from base import total_path

IMG1 = total_path + "lenna.jpg"
print(IMG1)
IMG2 = total_path + 'QuadradosColoridos.png'
print(IMG2)

BANDA_R = 2
BANDA_G = 1
BANDA_B = 0

W_NAME_ORI = 'Original'
W_NAME_C   = 'Canal C'
W_NAME_M   = 'Canal M'
W_NAME_Y   = 'Canal Y'

img1 = imread(IMG1)

imgCya = 255 - img1[:,:,BANDA_R]
imgMag = 255 - img1[:,:,BANDA_G]
imgYel = 255 - img1[:,:,BANDA_B]

imshow(W_NAME_ORI, img1)
imshow(W_NAME_C, imgCya)
imshow(W_NAME_M, imgMag)
imshow(W_NAME_Y, imgYel)

waitKey(0)

img2 = imread(IMG2)

imgCya = 255 - img2[:,:,BANDA_R]
imgMag = 255 - img2[:,:,BANDA_G]
imgYel = 255 - img2[:,:,BANDA_B]

imshow(W_NAME_ORI, img2)
imshow(W_NAME_C, imgCya)
imshow(W_NAME_M, imgMag)
imshow(W_NAME_Y, imgYel)

waitKey(0)
