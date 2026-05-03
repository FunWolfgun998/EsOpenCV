import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

# Carichiamo il classificatore delle facce
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Usa una foto di gruppo scaricata e chiamata 'gruppo.jpg'
img = cv2.imread('gruppo.jpg')
grigio = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Rileviamo le facce
facce = face_cascade.detectMultiScale(grigio, scaleFactor=1.1, minNeighbors=4)

# Disegniamo i rettangoli
for (x, y, w, h) in facce:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Scriviamo il totale in alto
testo = f"Persone trovate: {len(facce)}"
print(len(facce));
cv2.putText(img, testo, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

cv2.imshow('Rilevamento Gruppo', img)

# Salviamo il risultato
cv2.imwrite('gruppo_risultato.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()