import cv2
import pickle
import numpy as np
import csv
import time
import os
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier

import pyttsx3

def speak(str1):
    engine = pyttsx3.init()
    engine.say(str1)
    engine.runAndWait()


video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('.venv/Data/haarcascade_frontalface_default.xml')

# Load data
with open('.venv/Data/face_data.pkl', 'rb') as f:
    FACES = pickle.load(f)
with open('.venv/Data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

# Sanitize labels
LABELS = [label[0] if isinstance(label, list) else label for label in LABELS]

# Match length
min_len = min(len(FACES), len(LABELS))
FACES = np.array(FACES[:min_len]).reshape(min_len, -1)
LABELS = np.array(LABELS[:min_len])

print('Shape of Faces matrix --> ', FACES.shape)

# Train
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

COL_NAMES = ['NAME', 'TIME']

# Predict
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist=os.path.isfile(".venv/Attendance/Attendance_" + date + ".csv")
        cv2.putText(frame, str(output[0]), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 255, 50), 2)
        cv2.putText(frame, "Attendance", ((frame.shape[1]-cv2.getTextSize("Attendance", cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0][0])//2, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        cv2.putText(frame, "Press 'O' to take attendance", ((frame.shape[1]-cv2.getTextSize("Press 'O' to take attendance", cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)[0][0])//2, frame.shape[0]-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 1)
        attendance=[str(output[0]), str(timestamp)]
        
    cv2.imshow("Face Attendance", frame)
    k= cv2.waitKey(1)
    if k==ord('o'):
        speak("Attendance Taken..")
        time.sleep(5)
        if exist:
            with open(".venv/Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open(".venv/Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
            csvfile.close()
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
