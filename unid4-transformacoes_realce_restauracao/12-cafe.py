# Histograma
from cv2 import *
import numpy as np
from matplotlib import pyplot as plt

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

IMG = total_path + 'cafe.png'

W_NAME_ORI = 'Original'
W_NAME_TR1 = 'Limiarizacao 1'
W_NAME_TR2 = 'Limiarizacao 2'
W_NAME_FIN = 'Final'


img = imread(IMG, IMREAD_GRAYSCALE)
(w, h) = img.shape

"""
imshow(W_NAME_ORI, img)
waitKey(0)

plt.hist(img.ravel(), 256, [0,256])
plt.show() 
"""

ret, imgT = threshold(img, 146, 0, THRESH_TOZERO)
imshow(W_NAME_TR1, imgT)
waitKey(0)

plt.hist(imgT.ravel(), 256, [0,256])
plt.show() 


exit(0)
