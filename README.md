

# Face Detection and Authentication System

This project is a simple face detection and authentication system using Tkinter for the GUI and OpenCV for face detection. It allows a user to log in with a username and password, and once authenticated, it opens a camera feed with real-time face detection.

## Features

- **GUI Interface**: A simple login interface using Tkinter.
- **Face Detection**: Uses OpenCV's pre-trained Haar Cascade Classifier to detect faces in real-time.
- **Live Camera Feed**: Displays a video feed with detected faces outlined in rectangles.

## Prerequisites

- **Python 3.x**
- **Tkinter**: Comes bundled with Python's standard library.
- **OpenCV**: Install via pip:
  ```bash
  pip install opencv-python
  ```

## How to Run the Project

1. Ensure all prerequisites are installed.
2. Place the `haarcascade_frontalface_default.xml` file in the same directory as your script.
3. Run the script using:
   ```bash
   python <script_name>.py
   ```

## Code Overview

- **GUI Layout**: Created using Tkinter with input fields for `Username` and `Password`.
- **Login Logic**: On clicking "Login," the app checks if the username is **FXEC** and the password is **1234**.
- **Face Detection**: If the login is successful, the system initiates a camera feed with OpenCV, detecting faces in real-time.
  
## Face Detection Mechanism

The project uses OpenCV's Haar Cascade Classifier for face detection:
- **File**: `haarcascade_frontalface_default.xml` (OpenCV’s pre-trained face detection model).
- **Detection**: Converts the video frame to grayscale and detects faces, outlining each face with a red rectangle and displaying "person Found."

## Closing the Application

- **Close Button**: Shuts down the Tkinter application window.
- **Camera Feed**: Press "Q" or `q` to stop the video feed.

