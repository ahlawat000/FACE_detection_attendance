


# FACE_detection_attendance

FACE_detection_attendance is a Python-based face recognition attendance system that uses a webcam to detect and recognize faces in real time and automatically mark attendance. The system is designed for small-scale use such as classrooms, labs, or offices.

---

## Project Overview

This project uses computer vision techniques to:
- Detect faces from a live video stream
- Match detected faces with previously registered users
- Record attendance with name and timestamp in CSV format

Face recognition is handled using the `face_recognition` library built on top of dlib, while OpenCV is used for video capture and image processing.

---

## Features

- Real-time face detection using a webcam
- Face registration module to add new users
- Automatic attendance marking on successful recognition
- Attendance stored in CSV files
- Simple and modular Python codebase
- Virtual environment support

---

## Technologies Used

- Python 3
- OpenCV (cv2)
- face-recognition
- NumPy
- Pandas

---

## Project Structure

```

FACE_detection_attendance/
├── Attendance/               # Attendance CSV files
├── Data/                     # Stored face images / encodings
├── add_face.py               # Script to register new faces
├── app.py                    # Main attendance system
├── test.py                   # Testing / experimental script
├── background.png            # UI background image
├── requirements.txt          # Python dependencies
├── README.md
├── .gitignore
└── .venv/                    # Virtual environment (ignored in git)

````

---

## How the System Works

### 1. Face Registration
The `add_face.py` script captures face images from the webcam and associates them with a user-provided name. These images are stored and later used for recognition.

### 2. Face Recognition & Attendance
The `app.py` script:
- Starts the webcam feed
- Detects faces in each frame
- Encodes detected faces
- Compares them with stored encodings
- Marks attendance when a match is found

Attendance is recorded only once per session per person.

---

## Installation & Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/ahlawat000/FACE_detection_attendance.git
cd FACE_detection_attendance
````

### Step 2: Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Register faces

```bash
python add_face.py
```

* Enter the person’s name
* Capture face images using the webcam

### Start attendance system

```bash
python app.py
```

* The webcam will open
* Faces will be detected and recognized
* Attendance will be logged automatically

Press **q** to stop the program.

---

## Attendance Output

Attendance is stored in CSV format inside the `Attendance` directory with:

* Name
* Time of detection

Example:

```
Name,Time
Alice,09:12:45
Bob,09:15:10
```

---

## Limitations

* Requires good lighting for accurate recognition
* Designed for small datasets
* No database or cloud storage (CSV-based only)

---

## Future Improvements

* GUI-based interface
* Database integration
* Multiple camera support
* Web-based dashboard
* Improved face matching performance

---

## Author

**ahlawat000**

---



