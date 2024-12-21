import cv2
import mediapipe as mp
import time
from datetime import datetime
import pyscreenshot
import os
import threading
import tkinter as tk

def flash_effect():
    """Display a fullscreen white flash for 200ms."""
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg='white')
    root.attributes("-topmost", True)
    root.after(200, root.destroy)  # Flash lasts for 200 ms
    root.mainloop()


def take_screenshot():
    image = pyscreenshot.grab()
    
    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    try:
        # Determine the correct Pictures folder path based on the OS
        if os.name == "nt":  # Windows
            username = os.getenv("USERNAME")  # Get the Windows username
            pictures_folder = os.path.join(f"C:\\Users\\{username}\\Pictures")
            
            # Ensure the folder exists, create it if not
            if not os.path.exists(pictures_folder):
                os.makedirs(pictures_folder)
            
            path = os.path.join(pictures_folder, f"screenshot_{timestamp}.png")
        
        elif os.name == "posix":  # macOS or Linux
            home_dir = os.path.expanduser("~")
            if "darwin" in os.uname().sysname.lower():  # macOS
                path = os.path.join(home_dir, "Pictures", f"screenshot_{timestamp}.png")
            else:  # Linux
                path = os.path.join(home_dir, "Pictures/Screenshots", f"screenshot_{timestamp}.png")
                os.makedirs(os.path.dirname(path), exist_ok=True)
        else:
            # Default to the user's home directory for unknown OS
            path = os.path.join(os.path.expanduser("~"), f"screenshot_{timestamp}.png")
    except Exception as e:
        print(f"Error determining file path: {e}")
        path = os.path.expanduser(f"~/screenshot_{timestamp}.png")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save the screenshot
    image.save(path)
    print(f"Screenshot saved at {path}")


def capture_screenshot():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0) 

    prev_state = None  

    def is_palm_open(landmarks):
        fingers = [8, 12, 16, 20]
        open_fingers = 0
        for finger in fingers:
            if landmarks[finger].y < landmarks[finger - 2].y:  # Compare with lower joints
                open_fingers += 1
        return open_fingers >= 4

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        # Convert image to RGB (necessary as Mediapipe works with RGB images)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                if is_palm_open(landmarks):
                    current_state = "open"
                else:
                    current_state = "fist"

                if prev_state == "open" and current_state == "fist":
                    # Play sound and flash effect in parallel
                    try:
                        flash_effect()
                    except Exception as e:
                        print(f"Error playing sound or showing flash: {e}")
                    
                    # Take screenshot
                    take_screenshot()

                prev_state = current_state

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()


if __name__ == '__main__':
    capture_screenshot()
