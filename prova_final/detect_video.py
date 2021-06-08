import cv2
import numpy

# Abre a camera de video
video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Nao foi possivel abrir a camera!")
    exit(-1)
else:
    print("Camera aberta. Prosseguindo")

classTrain = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Faz a leitura de um quadro de video.
    ret, imgOrig = video.read()

    # detectando face com o classificador
    faceDet = classTrain.detectMultiScale(imgOrig, scaleFactor=1.1, minNeighbors=8, minSize=(30,30))

    for (x, y, w, h) in faceDet:
        cv2.rectangle(imgOrig, (x, y), (x + w, y + h), (0, 0, 255))

    # Mostrando a imagem original com o realce da face
    cv2.imshow("Frames do Vídeo/Câmera", imgOrig)

    # Pega o codigo ASCII da tecla pressionada, aguarda 1 milisegundo
    key = cv2.waitKey(1) & 0xFF
    
    # Verifica se ESC ou 'q' ou 'Q' foi pressionado
    if key in [27, ord("Q"), ord("q")]:
        break

cv2.destroyAllWindows()
video.release()