import numpy as np
import cv2 as cv
from cv2 import imshow, waitKey
from cv2.cv2 import imwrite


def pil2cv(image) -> np.ndarray:
    return cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)


def cv2pil(image: np.ndarray):
    pass


def test_img(img, print_pos=False):
    imshow('test', img)
    waitKey()
