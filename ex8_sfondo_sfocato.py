import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Creiamo una copia del frame completamente sfocata (kernel molto grande)
    sfocato = cv2.GaussianBlur(frame, (51, 51), 0)

    # 2. Troviamo le facce
    grigio = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facce = face_cascade.detectMultiScale(grigio, 1.1, 5)

    # 3. "Incolliamo" le facce nitide originali SOPRA lo sfondo sfocato
    for (x, y, w, h) in facce:
        # Estraiamo la faccia nitida dal frame originale
        faccia_nitida = frame[y:y+h, x:x+w]
        
        # La sovrascriviamo nella stessa posizione dell'immagine sfocata
        sfocato[y:y+h, x:x+w] = faccia_nitida

    cv2.imshow('Effetto Videochiamata', sfocato)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()