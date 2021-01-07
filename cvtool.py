import numpy as np
from cv2.cv2 import imshow, waitKey
import cv2


def pil2cv(img):
    return cv2.cv2.cvtColor(np.asarray(img), cv2.cv2.COLOR_RGB2BGR)


class MatchResult:
    matched = False
    pos = []

    def __str__(self):
        return "Result:%s&%s" % (self.matched, self.pos)


def match(source, image, similarity=0.85):
    # if type(image) == str:
    #     image = fpng(image)
    # image = np.array(image)

    res = cv2.cv2.matchTemplate(image, source, cv2.cv2.TM_CCOEFF_NORMED)
    _, sim, min_loc, max_loc = cv2.cv2.minMaxLoc(res)

    result = MatchResult()
    if sim > similarity:
        result.matched = True
        result.pos = max_loc

    return result


def test_img(img):
    imshow('test', img)
    waitKey()
