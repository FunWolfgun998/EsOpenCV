import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Variabile per memorizzare il frame precedente
frame_prec = None

# Soglia oltre la quale consideriamo il rumore un vero "movimento"
SOGLIA_PIXEL = 5000 

while True:
    ret, frame = cap.read()
    if not ret: break

    # Convertiamo in grigio e sfocchiamo molto per eliminare il rumore della webcam
    grigio = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grigio = cv2.GaussianBlur(grigio, (21, 21), 0)

    # Se è il primo ciclo, salviamo il frame e continuiamo
    if frame_prec is None:
        frame_prec = grigio
        continue

    # Calcoliamo la differenza assoluta tra il frame di adesso e quello di prima
    diff = cv2.absdiff(frame_prec, grigio)

    # Trasformiamo le differenze in Bianco (movimento) o Nero (fermo)
    # Se la differenza > 25, diventa 255 (bianco)
    _, soglia = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Contiamo quanti pixel bianchi ci sono
    pixel_in_movimento = cv2.countNonZero(soglia)

    if pixel_in_movimento > SOGLIA_PIXEL:
        cv2.putText(frame, "MOVIMENTO RILEVATO", (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow('Sorveglianza', frame)
    qcv2.imshow('Differenza (Dietro le quinte)', soglia)

    # Aggiorniamo il frame precedente
    frame_prec = grigio

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()