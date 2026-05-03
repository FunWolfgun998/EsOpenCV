import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2

img = cv2.imread('foto.jpg')

# Otteniamo dimensioni immagine (altezza, larghezza)
altezza, larghezza = img.shape[:2]

testo = "Creato da Me"
font = cv2.FONT_HERSHEY_SIMPLEX
scala = 1
colore = (0, 255, 255) # Giallo in BGR
spessore = 2

# BONUS: Calcoliamo quanto è grande il testo per posizionarlo in basso a destra
(text_width, text_height), baseline = cv2.getTextSize(testo, font, scala, spessore)

# X = larghezza totale - larghezza del testo - margine
x = larghezza - text_width - 10
# Y = altezza totale - margine
y = altezza - 10

cv2.putText(img, testo, (x, y), font, scala, colore, spessore)

cv2.imshow('Immagine con testo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()