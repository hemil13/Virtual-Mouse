Table of Contents
Overview
Features
Installation
Usage
Dependencies
Contributing
License
Acknowledgements
Overview


The Virtual Mouse using Hand Gestures is a Python-based project that allows users to control their computer's mouse using hand gestures. Utilizing computer vision techniques, the system recognizes specific gestures to move the cursor, perform clicks, and other mouse functions, creating a touch-free interface.


Features
Cursor Control: Move the cursor using hand gestures.
Click Actions: Perform left and right clicks with specific gestures.
Gesture Recognition: Recognizes different gestures for different actions.


Installation
To get started with the virtual mouse, follow these steps:

git clone https://github.com/Hemil13/Virtual-Mouse.git
cd virtual mouse


Install the required dependencies:

pip install mediapipe
pip install opencv
pip install pynput


Run the application:

python virtual_mouse.py


Usage
Once the application is running, hold your thumb, index and middle finger straight and rest two fingers folded in front of the webcam. The system will recognize specific gestures to control the mouse:

Move Cursor: Move your hand to control the cursor. Make sure the thumb is not stretched outwards.
Left Click: Stretch the thumbs outwards to lock the cursor position and curl the INDEX finger.
Right Click: Stretch the thumbs outwards to lock the cursor position and curl the MIDDLE finger.
Double Click: Stretch the thumbs outwards to lock the cursor position and curl the BOTH (Index and Middle Finger) finger.

For best results, ensure your hand is clearly visible to the camera and is well-lit.

Dependencies
Python 3.x
OpenCV: For computer vision tasks.
Mediapipe: For hand gesture recognition.
Numpy: For array operations.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
OpenCV
Mediapipe
