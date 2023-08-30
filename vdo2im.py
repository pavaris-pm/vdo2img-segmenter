import cv2
import os
import time
from pathlib import Path

print(os.getcwd())

# Open the video file
video_path = 'C:/Users/hp/Downloads/20230803-V1.avi'
vdo_name = video_path.split('/')[-1].split('.')[0]
print(vdo_name)
cap = cv2.VideoCapture(video_path)

# Specify the desired frame rate and duration
# since in opencv, 1 seconds equal to ~50 frames, we need to make some adjustment
desired_frame_rate = 50  # Frames per second (50 frames/sec)
desired_duration = 1  # Duration in seconds (cut every 1 sec)

# Calculate the number of frames to capture based on frame rate and duration
num_frames_to_capture = int(desired_frame_rate * desired_duration)
print('number of frames to capture:', num_frames_to_capture)

frames_captured = 0
seg_num = 0

# will be saved in Picture folder in WindowOS
save_dir = os.path.join(str(Path.home()),
                        'Pictures',
                        f'{vdo_name}_captured_frames')
print(save_dir)

# construct new folder
os.makedirs(save_dir, exist_ok=True)

while True:
    ret, frame = cap.read()

    # if not return any frame, stop the loop (video ended)
    if not ret:
        break

    # Process the frame (e.g., save it, display it, etc.)
    # You can also divide the frame into segments here

    frames_captured += 1

    if (frames_captured % num_frames_to_capture) == 0:
        # Display the processed frame (optional)
        # cv2.imshow('Frame', frame)

        # save frame into desired directory
        frame_filename = f'frame_{frames_captured:03d}.jpg'
        frame_path = os.path.join(save_dir, frame_filename)
        cv2.imwrite(frame_path, frame)
        seg_num += 1


print("Total frames:", frames_captured)
print("Total segmented frames:", seg_num)

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
