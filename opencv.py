# carregando bibliotecas do OpenCV e NumPy
from cv2 import *
import numpy as np


# exibindo uma mensagem no terminal
print('Hello World')

# inicializando uma font para escrita na imagem
font = FONT_HERSHEY_SIMPLEX

# criando uma imagem vazia (niveis de cinza)
img = np.zeros((200,200, 1), np.uint8)

# escrevendo na imagem
putText(img,"Hello World", (10,100), font, 1, 255, 1)

# exibindo a imagem
WNAME = 'Image of Hello World'
namedWindow(WNAME, WINDOW_AUTOSIZE)
imshow(WNAME, img)

# aguarda que ate que alguma tecla seja pressionada
waitKey(0)
