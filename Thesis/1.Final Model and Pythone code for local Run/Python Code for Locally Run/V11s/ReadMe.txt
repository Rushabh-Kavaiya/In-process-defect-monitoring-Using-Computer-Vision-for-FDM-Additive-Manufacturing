

README: In-Process Defect Monitoring Using Computer Vision for FDM-THD

Overview

This project implements real-time defect monitoring using computer vision and YOLO (You Only Look Once) for FDM-THD (Fused Deposition Modeling). It detects defects such as cracks, layer shifts, spaghetti, and stringing during 3D printing. When a defect is detected above a certain threshold, an alarm sound is played. The system provides a graphical user interface (GUI) for monitoring defects and adjusting sensitivity.

Requirements

Ensure you have the following dependencies installed before running the program:

Python Libraries:

Install the required dependencies using the following command:

pip install ultralytics pygame opencv-python numpy pillow tk

Additional Requirements:

- YOLO Model: `best.pt` (Ensure you have the trained YOLO model in the project directory.)
  
- Alarm Sound: `alarm.mp3` (Place an appropriate alarm sound file in the project directory.)
  
- Python Environment: Recommended to use PyCharm or a similar IDE.

Files in the Project

- `main.py` - The Python script to run the defect detection system.
  
- `best.pt` - The trained YOLO model file.
  
- `alarm.mp3` - The sound file played when defects exceed the threshold.

How to Run

1. Ensure the necessary files are in the project directory:
  
    - `main.py`
    
    - `best.pt`
    
    - `alarm.mp3`
  
2. Run the Python script: Open a terminal or command prompt and navigate to the project directory. Then execute:

    python main.py
  
3. Using the GUI:
  
    - The video feed will display real-time defect detection.
  
    - Defects detected will be logged in the table.
  
    - Adjust the confidence threshold using the slider.
  
    - Modify defect detection thresholds and apply changes.
  
    - Start or stop detection using the provided buttons.
  
    - Reset logs and alarms using the reset button.

Features

- Real-time defect detection using a YOLO-based deep learning model.
  
- Adjustable confidence threshold for detection sensitivity.
  
- Logging of detected defects with timestamps and confidence values.
  
- Customizable defect thresholds to set alert levels.
  
- Audio alerts when defect counts exceed thresholds.
  
- Graphical User Interface (GUI) for monitoring and control.

Troubleshooting

- If the webcam does not start, ensure it is properly connected and accessible, or change the code here for swapping the camera:

    cap = cv2.VideoCapture(1)

    Change to `0` if you want to swap the camera.
  
- If the YOLO model does not load, verify that `best.pt` is in the correct path.
  
- If sound alerts do not work, ensure `alarm.mp3` is available and `pygame.mixer` is installed.
  
- If an error occurs, check dependencies using `pip list` and install missing packages.

Notes

- Press 'q' to manually exit the program if needed.
  
- Ensure system permissions allow access to the camera and audio output.
