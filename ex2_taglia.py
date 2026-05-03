import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2

img = cv2.imread('foto.jpg')

# Slicing su matrice NumPy: img[y_inizio:y_fine, x_inizio:x_fine]
# NOTA: Cambia questi valori in base alla dimensione della tua "foto.jpg"
ritaglio = img[100:300, 150:400] 

cv2.imshow('Immagine intera', img)
cv2.imshow('Ritaglio', ritaglio)

# Salva il ritaglio come file separato
cv2.imwrite('ritaglio_salvato.jpg', ritaglio)
print("Immagine ritagliata e salvata con successo!")

cv2.waitKey(0)
cv2.destroyAllWindows()