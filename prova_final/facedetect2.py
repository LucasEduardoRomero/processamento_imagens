import cv2
import numpy

total_path = "C:\\Users\\Lucas\\Projects\\processamento_imagens\\prova_final\\"

images = ['faceBeautifulWoman.png', 'faces.png', 'me.jpg']
imgSave = ['faceBeautifulWoman-res.png', 'faces-res.png', 'me-res.jpg']

# Lendo o classificador treinado:
classTrain = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for i in range(len(images)):
    # Lendo a imagem (Imagem estatica) 
    imgOrig = cv2.imread(total_path + images[i])

    # Convertendo para cinza
    imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

    # Detectando com o classificador
    faceDet = classTrain.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=8, minSize=(30,30))

    # Quantidade de Faces Detectadas
    print("Faces detectadas: %d em '%s'" % (len(faceDet), images[i]))

    # Realçando a face detectadas
    for (x, y, w, h) in faceDet:
        cv2.rectangle(imgOrig, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    # Mostrando a imagem original com o realce da face
    cv2.imshow("Realce da(s) face(s) encontrada(s)", imgOrig)
    cv2.imwrite(imgSave[i], imgOrig)
    cv2.waitKey()
    