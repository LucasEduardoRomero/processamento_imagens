from cv2 import *
import numpy as np

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

IMG_ORIG = total_path + 'balantidium-coli.jpg'
#IMG_ORIG = 'oldwall.jpg'
IMG_TEMP = total_path + 'imgTmp.jpg'

W_ORIG = 'Imagem Original'
W_TEMP = 'Imagem Resultante'
W_RESP = 'Imagem Diferenca'

imgOrig = imread(IMG_ORIG, IMREAD_COLOR)
imgTmp = imgOrig.copy()
imgResp = (imgOrig - imgTmp)

# definindo as janelas das imagens
namedWindow(W_ORIG, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_ORIG, imgOrig)
resizeWindow(W_ORIG, 320, 240)
moveWindow(W_ORIG, 10, 10)

namedWindow(W_RESP, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_RESP, imgResp)
resizeWindow(W_RESP, 320, 240)
moveWindow(W_RESP, 380, 10)

namedWindow(W_TEMP, WINDOW_NORMAL or WINDOW_KEEPRATIO)
imshow(W_TEMP, imgTmp)
resizeWindow(W_TEMP, 320, 240)
moveWindow(W_TEMP, 10, 380)
k = (waitKey(0) %  0xFF)
n = 0
dif = difA = 0.0
while (k != 27):
	# exibindo as imagens
	imwrite(IMG_TEMP, imgTmp)
	imgTmp = imread(IMG_TEMP, IMREAD_COLOR)
	n = n + 1
	print("Imagem %d" % n)

	# definindo as janelas das imagens
	imshow(W_ORIG, imgOrig)
	imshow(W_TEMP, imgTmp)
	imgResp = (imgOrig - imgTmp)
	imshow(W_RESP, imgResp)
	k = (waitKey(0) %  0xFF)
