import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Smoothing dei colori mantenendo i bordi (Bilateral Filter)
    # Rende l'immagine simile a un dipinto/cartoon
    colore = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)

    # 2. Troviamo i bordi con Canny
    grigio = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bordi = cv2.Canny(grigio, 50, 150) # Risultato: bordi BIANCHI su sfondo NERO

    # 3. Invertiamo i bordi (vogliamo bordi NERI su sfondo BIANCO per il fumetto)
    bordi_invertiti = cv2.bitwise_not(bordi)

    # 4. Uniamo i colori appiattiti con i bordi neri
    # bitwise_and unisce le immagini usando la maschera (mantiene il colore solo dove la maschera è bianca)
    fumetto = cv2.bitwise_and(colore, colore, mask=bordi_invertiti)

    cv2.imshow('Filtro Fumetto', fumetto)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()