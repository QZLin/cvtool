import numpy as np
import cv2
from cv2.cv2 import imshow, waitKey


def pil2cv(img):
    return cv2.cv2.cvtColor(np.asarray(img), cv2.cv2.COLOR_RGB2BGR)


def test_img(img):
    imshow('test', img)
    waitKey()
