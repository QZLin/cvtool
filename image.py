import numpy as np
import cv2 as cv
from cv2 import imshow, waitKey


def pil2cv(image):
    return cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)


def cv2pil(image):
    pass


def test_img(img):
    imshow('test', img)
    waitKey()
