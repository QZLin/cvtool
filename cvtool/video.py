import numpy as np
import cv2 as cv


def simple_player(path, interval=30):
    cap = cv.VideoCapture(path)
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            break
        cv.imshow('simple_player', frame)
        if cv.waitKey(interval) == 113:  # ord('q') -> 113
            break
    cap.release()
    cv.destroyAllWindows()


def read(path):
    pass
