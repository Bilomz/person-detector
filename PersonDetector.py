import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.resize(frame, (640, 480))
    

    people, _ = hog.detectMultiScale(frame)

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for (x, y, w, h) in people:
        if w < 60 or h < 120:
            continue
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.putText(frame, "Person", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(frame, f"Timestamp: {current_time}", (10,470),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


    cv2.imshow("Press Q to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    
