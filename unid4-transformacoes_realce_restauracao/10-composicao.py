from cv2 import *
import numpy as np

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

#IMG_ORIG = 'balantidium-coli.jpg'
IMG_ORIG = total_path + 'oldwall.jpg'
IMG_LOGO = total_path + 'UFMT.jpg'

W_ORIG = 'Imagem Original'
W_LOGO = 'Imagem do Logo'
W_RESP = 'Imagem resultante'

LOGO_W = 96
LOGO_H = 64

# Leitura das duas imagens
imgOrig = imread(IMG_ORIG, IMREAD_COLOR)
imgLogo = imread(IMG_LOGO, IMREAD_GRAYSCALE)

imgLogo = resize(imgLogo, (LOGO_W, LOGO_H), INTER_NEAREST)
imgLogo = 255 - imgLogo	# invertendo a imagem de logo
ret, imgLogo = threshold(imgLogo, 100, 255, THRESH_BINARY)

# definindo as janelas das imagens
namedWindow(W_ORIG, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_ORIG, imgOrig)
resizeWindow(W_ORIG, 320, 240)
moveWindow(W_ORIG, 10, 10)

namedWindow(W_LOGO, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_LOGO, imgLogo)
resizeWindow(W_LOGO, LOGO_W, LOGO_H)
moveWindow(W_LOGO, 380, 10)

# regiao de interesse (ROI)
imgResp = imgOrig[-LOGO_H:, -LOGO_W:]

namedWindow(W_RESP, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_RESP, imgResp)
resizeWindow(W_RESP, 320, 240)
moveWindow(W_RESP, 4, 300)

# exibindo as imagens
waitKey(0)
DEPTH  = 36

for b in range(3):
	# Reservar DEPTH pontos de brilho para a inclusão da logo
	imgResp[:,:,b] = 255-imgResp[:,:,b]
	ret, imgResp[:,:,b] = threshold(imgResp[:,:,b], 255-DEPTH , 255-DEPTH , THRESH_TRUNC)
	imgResp[:,:,b] = 255-imgResp[:,:,b]
	#-----------------------------------------
	imgResp[:,:,b] = imgResp[:,:,b] - DEPTH *(imgLogo/255)

# definindo as janelas das imagens
namedWindow(W_ORIG, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_ORIG, imgOrig)
resizeWindow(W_ORIG, 320, 240)
moveWindow(W_ORIG, 10, 10)

namedWindow(W_RESP, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_RESP, imgResp)
resizeWindow(W_RESP, 320, 240)
moveWindow(W_RESP, 4, 300)

# exibindo as imagens
waitKey(0)

