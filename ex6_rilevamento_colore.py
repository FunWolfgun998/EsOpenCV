import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Convertiamo in HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. Definiamo i limiti per il colore VERDE in HSV
    # H (Tinta): ~40 a 80 è verde. S (Saturazione): 40-255. V (Valore): 40-255
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # 3. Creiamo la maschera: bianco dove c'è verde, nero altrove
    maschera = cv2.inRange(hsv, lower_green, upper_green)

    cv2.imshow('Originale', frame)
    cv2.imshow('Maschera Verde', maschera)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()