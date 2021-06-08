# carregando bibliotecas do OpenCV e NumPy
from cv2 import *
from numpy import *

# Nome do arquivo
IMG_PONTE = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\PonteSergioMota.jpg"

# Nome das Janelas
W_NAME_ORIG	= "Imagem Original"
W_4NN	= "1/4 Nearest"
W_4LI	= "1/4 Linear"
W_4AR	= "1/4 Inter Area"
W_4BC	= "1/4 Bicubic"
W_4LC	= "1/4 Lanczos4"

# Leitura do arquivo de imagem
imPonte = imread(IMG_PONTE, IMREAD_GRAYSCALE)

# Exibe a imagem
imshow(W_NAME_ORIG, imPonte)
waitKey(0)
destroyWindow(W_NAME_ORIG)

# obtendo altura e largura da imagem monocromatica
(Altura, Largura) = imPonte.shape

# Reducao para 1/4 da imagem original usando metodos diferentes
# O uso de cv2 aqui se deve ao fato de existir outra funcao global
# de mesmo nome no Python, o que provocaria erro sem o cv2.
im4NN = cv2.resize(imPonte, (int(Largura/2), int(Altura/2)), INTER_NEAREST)
im4LI = cv2.resize(imPonte, (int(Largura/2), int(Altura/2)), INTER_LINEAR)
im4BC = cv2.resize(imPonte, (int(Largura/2), int(Altura/2)), INTER_CUBIC)
im4AR = cv2.resize(imPonte, (int(Largura/2), int(Altura/2)), INTER_AREA)
im4LC = cv2.resize(imPonte, (int(Largura/2), int(Altura/2)), INTER_LANCZOS4)

imshow(W_4NN, im4NN)
imshow(W_4LI, im4LI)
imshow(W_4BC, im4BC)
imshow(W_4AR, im4AR)
imshow(W_4LC, im4LC)
waitKey(0)

im4NN = cv2.resize(im4NN, (int(0.9*Largura), int(0.9*Altura)), INTER_NEAREST)
im4LI = cv2.resize(im4LI, (int(0.9*Largura), int(0.9*Altura)), INTER_LINEAR)
im4BC = cv2.resize(im4BC, (int(0.9*Largura), int(0.9*Altura)), INTER_CUBIC)
im4AR = cv2.resize(im4AR, (int(0.9*Largura), int(0.9*Altura)), INTER_AREA)
im4LC = cv2.resize(im4LC, (int(0.9*Largura), int(0.9*Altura)), INTER_LANCZOS4)

imshow(W_4NN, im4NN)
imshow(W_4LI, im4LI)
imshow(W_4BC, im4BC)
imshow(W_4AR, im4AR)
imshow(W_4LC, im4LC)
waitKey(0)


exit(0)
