# ScreenRecoder
This Python script is a screen recording tool that captures the entire display screen in real-time and saves it as an MP4 video file. It is designed to work on Windows systems and is built using modules like PIL, OpenCV, NumPy, and pywin32.

Functionality:
Captures the full screen continuously.

Saves the recording in .mp4 format with a timestamped filename.

Shows a live preview of the recording using OpenCV.

Stops recording when the user presses the s key.

Modules Used:
datetime: For generating unique filenames based on the current date and time.

PIL.ImageGrab: For taking screenshots of the screen.

numpy: For image data conversion between formats.

cv2 (OpenCV): For previewing and saving video frames.

win32api.GetSystemMetrics: For getting the screen resolution.
