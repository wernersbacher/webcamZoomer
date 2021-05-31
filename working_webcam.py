import pyvirtualcam
import cv2
import effects

FPS = 30
WIDTH = 1280
HEIGHT = 720

# initialize webcam capture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


with pyvirtualcam.Camera(width=1280, height=720, fps=FPS, fmt=pyvirtualcam.PixelFormat.BGR) as cam:
    print(f'Using virtual camera: {cam.device}')

    while True:
        success, img = cap.read()

        cam.send(effects.zoom(img))
        cam.sleep_until_next_frame()
