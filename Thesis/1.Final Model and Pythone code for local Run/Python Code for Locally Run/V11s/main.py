import cv2
from ultralytics import YOLO
import pygame
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

# Load YOLO model
model_path = "best.pt"  # Replace with actual model path
model = YOLO(model_path)

# Initialize sound alerts
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("alarm.mp3")  # Replace with actual sound file

# Predefined defect names and initial thresholds
DEFECT_NAMES = ["Cracks", "Layer-shift", "Spaghetti", "Stringging"]
detection_log = {name: (0, 0.0, "--:--:--") for name in DEFECT_NAMES}
thresholds = {name: 50 for name in DEFECT_NAMES}  # Default thresholds

# GUI Initialization
root = tk.Tk()
root.title("In-process defect monitoring Using Computer Vision for FDM- THD")
root.geometry("1000x600")

# Global confidence threshold (default = 0.5)
confidence_threshold = tk.DoubleVar(value=0.5)

# Video feed frame
video_label = tk.Label(root)
video_label.pack(pady=10)

# Frame for log table and threshold settings
log_frame = tk.Frame(root)
log_frame.pack(fill="both", expand=True, pady=10)

# Detection log table
columns = ("Defect Type", "Count", "Confidence", "Timestamp", "Threshold")
log_table = ttk.Treeview(log_frame, columns=columns, show="headings", height=10)
for col in columns:
    log_table.heading(col, text=col)
    log_table.column(col, width=150)
log_table.pack(side="left", fill="both", expand=True)

# Frame for threshold inputs
threshold_frame = tk.Frame(log_frame)
threshold_frame.pack(side="right", fill="y")

threshold_entries = {}

def update_thresholds():
    """Update the thresholds dictionary based on user input."""
    for defect, entry in threshold_entries.items():
        try:
            thresholds[defect] = int(entry.get())
        except ValueError:
            thresholds[defect] = 50  # Default to 50 if input is invalid

# Populate threshold inputs beside the table
for defect in DEFECT_NAMES:
    frame = tk.Frame(threshold_frame)
    frame.pack(pady=5)
    tk.Label(frame, text=defect, font=("Arial", 10)).pack(side="left")
    entry = tk.Entry(frame, width=5)
    entry.insert(0, "50")  # Default threshold
    entry.pack(side="left")
    threshold_entries[defect] = entry

# Apply button to update thresholds
apply_button = tk.Button(threshold_frame, text="Apply", command=update_thresholds)
apply_button.pack(pady=5)

# Buttons and Confidence Threshold Slider at the Bottom
button_frame = tk.Frame(root)
button_frame.pack(pady=10, fill="x")

# Confidence Threshold Slider
conf_frame = tk.Frame(button_frame)
conf_frame.pack(side="left", padx=10)
tk.Label(conf_frame, text="Confidence Threshold:", font=("Arial", 10)).pack(side="left")
conf_slider = tk.Scale(conf_frame, from_=0.1, to=1.0, resolution=0.05, orient="horizontal",
                       variable=confidence_threshold)
conf_slider.pack(side="left", padx=10)

# Reset button
def reset_logs():
    """Clear all logs and stop sound."""
    global detection_log
    detection_log = {name: (0, 0.0, "--:--:--") for name in DEFECT_NAMES}
    alert_sound.stop()
    log_table.delete(*log_table.get_children())
    for defect in DEFECT_NAMES:
        log_table.insert("", "end", values=(f"DEFECT: {defect}", 0, "-", "--:--:--", thresholds[defect]))

reset_button = tk.Button(button_frame, text="Reset", command=reset_logs, font=("Arial", 12), bg="red", fg="white")
reset_button.pack(side="left", padx=10)

# Start/Stop Buttons
running = False

def start_detection():
    global running
    running = True
    threading.Thread(target=process_frame, daemon=True).start()

def stop_detection():
    global running
    running = False

start_button = tk.Button(button_frame, text="Start", command=start_detection, font=("Arial", 12), bg="green", fg="white")
start_button.pack(side="left", padx=10)

stop_button = tk.Button(button_frame, text="Stop", command=stop_detection, font=("Arial", 12), bg="black", fg="white")
stop_button.pack(side="left", padx=10)

# Sound alert function
def play_alert_sound():
    """Play alert sound twice."""
    alert_sound.play()
    time.sleep(1)
    alert_sound.play()

# Update GUI function
def update_gui(frame):
    """Convert OpenCV frame to Tkinter format and update video label."""
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    video_label.config(image=img)
    video_label.image = img

# Update log table function
def update_log():
    """Update the detection log in the GUI."""
    log_table.delete(*log_table.get_children())
    for defect in DEFECT_NAMES:
        count, conf, timestamp = detection_log.get(defect, (0, 0.0, "--:--:--"))
        log_table.insert("", "end", values=(
            f"DEFECT: {defect}", count, f"{conf:.2f}" if count > 0 else "-", timestamp, thresholds[defect]))

# Process video frame and detect defects
def process_frame():
    global running

    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Could not access the webcam")
        return

    while running:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        results = model(frame)
        current_time = time.strftime("%H:%M:%S")

        # Defect detection
        for result in results:
            for box in result.boxes:
                conf = box.conf[0].item()
                if conf < confidence_threshold.get():
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                label = model.names[cls].replace("DEFECT- ", "").strip()

                if label in DEFECT_NAMES:
                    current_count = detection_log[label][0] + 1
                    detection_log[label] = (current_count, conf, current_time)

                    # Draw bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} ({current_count})",
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 255, 0), 2)

                    # Trigger alert at every multiple of the defect's threshold
                    if current_count % thresholds[label] == 0:
                        play_alert_sound()

        # Update GUI components
        update_gui(frame)
        update_log()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Initialize table with defect names
reset_logs()

# Run the GUI
root.mainloop()
