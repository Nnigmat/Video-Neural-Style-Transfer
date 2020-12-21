import cv2
import numpy as np
import os

# Playing video from file:
def split_video(path, dest_path, start_index):
    cap = cv2.VideoCapture(path)

    try:
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = start_index
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Saves image of the current frame in jpg file
        name = f'./{dest_path}/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return currentFrame

'''
files = ['1_ready.mp4', '2_ready.mp4', '3_ready.mp4', '4_ready.mp4']
counter = 0
for f in files:
    counter = split_video(f, counter)
'''

split_video('fire_ready.mp4', 'fire', 0)
