from cv2 import *
import numpy as np

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

IMG1 = total_path + 'lenna.jpg'
IMG2 = total_path + 'QuadradosColoridos.png'

BANDA_R = 2
BANDA_G = 1
BANDA_B = 0

W_NAME_ORI = 'Original'
W_NAME_R   = 'Canal R'
W_NAME_G   = 'Canal G'
W_NAME_B   = 'Canal B'

img1 = imread(IMG1)
imshow(W_NAME_ORI, img1)

# Exibindo as bandas da Lenna separadamente
imgRed = img1[:,:,BANDA_R]
imgGre = img1[:,:,BANDA_G]
imgBlu = img1[:,:,BANDA_B]

imshow(W_NAME_R, imgRed)
imshow(W_NAME_G, imgGre)
imshow(W_NAME_B, imgBlu)

waitKey(0)

# Exibindo as bandas da Lenna separadamente em cores
imgRedC = img1.copy()
imgGreC = img1.copy()
imgBluC = img1.copy()

imgRedC[:,:,BANDA_R] = imgRed
imgRedC[:,:,BANDA_G] = 0*imgRed
imgRedC[:,:,BANDA_B] = 0*imgRed

imgGreC[:,:,BANDA_G] = imgGre
imgGreC[:,:,BANDA_R] = 0*imgGre
imgGreC[:,:,BANDA_B] = 0*imgGre

imgBluC[:,:,BANDA_B] = imgBlu
imgBluC[:,:,BANDA_R] = 0*imgBlu
imgBluC[:,:,BANDA_G] = 0*imgBlu

imshow(W_NAME_R, imgRedC)
imshow(W_NAME_G, imgGreC)
imshow(W_NAME_B, imgBluC)

waitKey(0)

# Exibindo as bandas do QuadradosColoridos separadamente
img2 = imread(IMG2)
imshow(W_NAME_ORI, img2)

imgRed = img2[:,:,BANDA_R]
imgGre = img2[:,:,BANDA_G]
imgBlu = img2[:,:,BANDA_B]

imshow(W_NAME_R, imgRed)
imshow(W_NAME_G, imgGre)
imshow(W_NAME_B, imgBlu)

waitKey(0)

# Exibindo as bandas do QuadradosColoridos separadamente em cores
imgRedC = img2.copy()
imgGreC = img2.copy()
imgBluC = img2.copy()

imgRedC[:,:,BANDA_R] = imgRed
imgRedC[:,:,BANDA_G] = 0*imgRed
imgRedC[:,:,BANDA_B] = 0*imgRed

imgGreC[:,:,BANDA_G] = imgGre
imgGreC[:,:,BANDA_R] = 0*imgGre
imgGreC[:,:,BANDA_B] = 0*imgGre

imgBluC[:,:,BANDA_B] = imgBlu
imgBluC[:,:,BANDA_R] = 0*imgBlu
imgBluC[:,:,BANDA_G] = 0*imgBlu

imshow(W_NAME_R, imgRedC)
imshow(W_NAME_G, imgGreC)
imshow(W_NAME_B, imgBluC)

waitKey(0)
