import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # cv2.flip richiede il frame e un codice:
    # 1 = capovolgimento orizzontale (asse y) -> Effetto specchio
    # 0 = capovolgimento verticale (asse x)
    # -1 = capovolgimento su entrambi gli assi
    frame_specchio = cv2.flip(frame, 1)
    
    cv2.imshow('Webcam Specchio', frame_specchio)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()