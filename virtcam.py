import pyvirtualcam
import cv2
import effects
import numpy as np


class VirtualCam:

    # TODO: manager für boolean, oder einfach nur threading

    def __init__(self, zoom=1):
        # No need for locking on that variables, as it's "thread safe", as long we only write from one thread!
        super().__init__()
        self.stopped = False
        self.paused = False

        self.cap = None
        self.zoom = zoom

        # constants
        self.FPS = 30
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.EMPTY_IMAGE = np.zeros((self.HEIGHT, self.WIDTH, 3), np.uint8)

    def initCaptureDevice(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def run(self):
        self.initCaptureDevice()
        with pyvirtualcam.Camera(width=1280, height=720, fps=self.FPS, fmt=pyvirtualcam.PixelFormat.BGR) as cam:
            print(f'Using virtual camera: {cam.device}')

            while not self.stopped:
                if not self.paused:  # only copy image if NOT paused!
                    success, img = self.cap.read()
                else:
                    img = self.EMPTY_IMAGE

                cam.send(effects.zoom(img, self.zoom))
                cam.sleep_until_next_frame()
            print("Stopped camera capturing!")

    def pause(self):
        print("called vcam pause")
        self.paused = True

    def cont(self):
        self.paused = False

    def stop(self):
        self.stopped = True

    def addZoom(self, zoom_delta):
        self.zoom += zoom_delta
        if self.zoom > 1:
            self.zoom = 1
        elif self.zoom < 0:
            self.zoom = 0


if __name__ == '__main__':
    cam = VirtualCam()
    cam.addZoom(-0.13)
    cam.run()
