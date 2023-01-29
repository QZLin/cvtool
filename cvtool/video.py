import numpy as np
import cv2 as cv


def simple_player(path, interval=30, filter_=None):
    cap = cv.VideoCapture(path)
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            break
        if filter_ is not None:
            frame = filter_(frame)
        cv.imshow('simple_player', frame)
        if cv.waitKey(interval) == 113:  # ord('q') -> 113
            break
    cap.release()
    cv.destroyAllWindows()


def example_filter(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def read(path):
    pass
