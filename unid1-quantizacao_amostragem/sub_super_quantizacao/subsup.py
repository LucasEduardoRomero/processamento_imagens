# carregando bibliotecas do OpenCV e NumPy
from cv2 import *
from numpy import *

# Nome do arquivo
IMG_PONTE = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\PonteSergioMota.jpg"

# Nome da Janela
W_NAME_ORIG = "Imagem Original"
W_7BITS = "Quantizado em 7 bits"
W_6BITS = "Quantizado em 6 bits"
W_5BITS = "Quantizado em 5 bits"
W_4BITS = "Quantizado em 4 bits"
W_3BITS = "Quantizado em 3 bits"
W_2BITS = "Quantizado em 2 bits"
W_1BITS = "Quantizado em 1 bits"

# Leitura do arquivo de imagem
imPonte = imread(IMG_PONTE, IMREAD_GRAYSCALE)
(Alt, Larg) = imPonte.shape

# Exibe a imagem
imshow(W_NAME_ORIG, imPonte)
waitKey(0)
destroyWindow(W_NAME_ORIG)

# Quantizando as imagens 
#   >> n => subquantiza a imagem em n bits
#   << n => superquantiza a imagem em n bits
im7Bits = ((imPonte >> 1) << 1)
im6Bits = ((imPonte >> 2) << 2)
im5Bits = ((imPonte >> 3) << 3)
im4Bits = ((imPonte >> 4) << 4)
im3Bits = ((imPonte >> 5) << 5)
im2Bits = ((imPonte >> 6) << 6)
im1Bits = ((imPonte >> 7) << 7)

imshow(W_7BITS, im7Bits)
imshow(W_6BITS, im6Bits)
imshow(W_5BITS, im5Bits)
imshow(W_4BITS, im4Bits)
imshow(W_3BITS, im3Bits)
imshow(W_2BITS, im2Bits)
imshow(W_1BITS, im1Bits)
waitKey(0)

exit(0)