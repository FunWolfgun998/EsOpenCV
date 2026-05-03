import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2
import numpy as np

# Carica l'immagine
img = cv2.imread('foto.jpg')

# HINT NumPy: Un pixel con valore 200 diventa 255 - 200 = 55.
# Dato che img è una matrice NumPy, possiamo fare 255 - img senza usare cicli!
negativo = 255 - img

cv2.imshow('Originale', img)
cv2.imshow('Negativo', negativo)

cv2.waitKey(0)
cv2.destroyAllWindows()