# Virtual Mouse Project

## Overview

The Virtual Mouse Project is a Python-based application that utilizes hand tracking and computer vision techniques to control the computer mouse using hand gestures. The project incorporates the [Mediapipe](https://mediapipe.dev/) library for hand tracking and [Autopy](https://pypi.org/project/autopy/) for mouse control.

## Features

- **Hand Tracking:** Utilizes the Mediapipe library to detect and track hand landmarks.
- **Virtual Mouse Control:** Moves and clicks the computer mouse based on the position and gestures of the user's hand.
- **Finger Detection:** Recognizes gestures such as finger movements and distances between fingers.
- **Frame Rate Display:** Shows the frame rate of the webcam feed for monitoring performance.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/virtual-mouse-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd virtual-mouse-project
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:

   ```bash
   python virtual_mouse.py
   ```

2. Position your hand in front of the webcam to control the virtual mouse.
3. Use the specified gestures to move and click the mouse.

## Configuration

- The `virtual_mouse.py` script includes parameters such as webcam dimensions, frame reduction, and smoothening factor that can be adjusted for optimal performance.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
