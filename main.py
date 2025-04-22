import datetime # import the datetime module
from PIL import ImageGrab # It helps to grab image from the screen
import numpy as np # It helps to import the array
import cv2 # It helps to capture the image and display
from win32api import GetSystemMetrics # It helps us to capture the image of system size

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# It helps to make a dynamic file
file_name=f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # It helps us with encoding
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height)) # Saving the video in file

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    
    # Once you have image, you have to convert it into the array
    img_np = np.array(img) # It stores image-related information
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # It helps to convert image color into its original color
    
    cv2.imshow('Screen Recorder', img_final) # It helps to show the image
    
    captured_video.write(img_final)
    
    if cv2.waitKey(10) == ord('s'):
        # It helps to stop the recording
        break

captured_video.release()
cv2.destroyAllWindows()