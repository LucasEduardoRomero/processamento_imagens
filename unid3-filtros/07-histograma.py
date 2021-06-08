# Histograma
from cv2 import *
import numpy as np
from matplotlib import pyplot as plt

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\assets\\"

IMG = total_path + 'hand-ir.pgm'

W_NAME_ORI = 'Original'
W_NAME_TR1 = 'Limiarizacao 1'
W_NAME_TR2 = 'Limiarizacao 2'
W_NAME_FIN = 'Final'


img = imread(IMG, IMREAD_GRAYSCALE)
(w, h) = img.shape


imshow(W_NAME_ORI, img)

"""
hist = calcHist([img], [0], None, [256], [0,256])
plt.hist(img.ravel(), 256, [0,256])
plt.show() 

plt.plot(hist)
plt.show()
"""

ret, imgT = threshold(img, 50, 255, THRESH_TOZERO)
#imshow(W_NAME_TR1, imgT)

ret, imgT2 = threshold(imgT, 180, 255, THRESH_TOZERO_INV)
imshow(W_NAME_TR2, imgT2)
waitKey(0)

plt.hist(imgT2.ravel(), 256, [0,256])
plt.show() 

imgT = equalizeHist(imgT2)
imshow(W_NAME_FIN, imgT)
waitKey(0)

plt.hist(imgT.ravel(), 256, [0,256])
plt.show() 


exit(0)
