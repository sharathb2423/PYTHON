import cv2 as cv
import time, datetime

cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_fullbody_default.xml")

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv.VideoWriter_fourcc(*"mp4v")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 3

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    bodies = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, width, height) in faces:
        cv.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 255), 5)

    if len(faces) + len(bodies) > 0:
        if detection is True:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started recording!")

    elif detection is True:
        if timer_started is True:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stopped recording!")

        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    cv.imshow("Security Cammera", frame)
    if cv.waitKey(1) == ord("q"): break

out.release()
cap.release()
cv.destroyAllWindows()