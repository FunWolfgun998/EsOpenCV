import os

os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2
from datetime import datetime # Modulo per data e ora

cap = cv2.VideoCapture(0)
print("Premi 's' per salvare una foto, 'q' per uscire.")

while True:
    ret, frame = cap.read()
    if not ret: break

    # Mostriamo a schermo un'istruzione
    cv2.putText(frame, "Premi 's' per scattare", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow('Cattura Foto', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        # Generiamo un timestamp del tipo: 20260503_183045
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_file = f"foto_{timestamp}.jpg"
        cv2.imwrite(nome_file, frame)
        print(f"Salvato: {nome_file}")

cap.release()
cv2.destroyAllWindows()