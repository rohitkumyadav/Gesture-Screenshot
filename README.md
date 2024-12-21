# Screenshot Capture Using Hand Gestures

This project enables users to take screenshots using hand gestures detected via a webcam. It leverages the MediaPipe library for hand detection and OpenCV for video processing. The logic uses the transition of hand gestures (from an open palm to a fist) to trigger a screenshot.

## Features

- Real-time hand gesture recognition.
- Screenshot capture when an open palm transitions to a fist gesture.
- Configurable and extensible for other gesture-based controls.

## Requirements

To run this project, you need the following dependencies:

- Python 3.7+
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- A library or function for taking screenshots, such as `ss_taker`. Replace `take_screenshot` in the code with your screenshot functionality.

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages:
   ```bash
   pip install opencv-python mediapipe
   ```
3. Ensure your Python environment includes the `ss_taker` library or a custom implementation for taking screenshots.

## Usage

1. Save the script to a file, e.g., `gesture_screenshot.py`.
2. Run the script:
   ```bash
   python gesture_screenshot.py
   ```
3. The webcam will activate, and the program will begin detecting hand gestures.
4. Show an open palm to the camera, then transition to a fist gesture to capture a screenshot.
5. Press `q` to quit the program.

## Usage Example

```python
from project_Screenshot.r_screenshot import take_screenshot , capture_screenshot

# to take normal screenshot
take_screenshot()

# for Gesture recognizer screenshot
capture_screenshot()
```

## How It Works

### Gesture Detection

The script uses the MediaPipe library to detect hand landmarks and determine whether the hand is open or closed:
- **Open palm:** All fingers extended (based on landmark positions).
- **Fist:** All fingers closed.

### Screenshot Trigger

When the script detects a transition from an open palm to a fist, it calls the `take_screenshot()` function to capture the current screen.

### Core Functions
#### `is_palm_open(landmarks)`
Determines whether the hand is open by comparing the positions of finger landmarks.

#### `capture_screenshot()`
Main function that:
- Captures video from the webcam.
- Processes each frame for hand landmarks.
- Detects gesture transitions and triggers screenshot capture.

## Customization
You can modify the script to:
- Recognize additional gestures.
- Perform other actions (e.g., send alerts or control devices) based on gestures.

## Limitations
- Requires a clear view of the hand for accurate detection.
- Designed for a single hand; might need enhancements for multi-hand detection.

## Acknowledgments
- [OpenCV](https://opencv.org/) for image processing.
- [MediaPipe](https://mediapipe.dev/) for hand landmark detection.

## To View Full Code
- [Github](https://github.com/rohitkumyadav/Gesture-Screenshot.git) to view full source code

## Contributing
Contributions are welcome! If you have ideas for improvements or additional features, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

