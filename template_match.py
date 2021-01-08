import numpy as np
import cv2


class MatchResult:
    matched = False
    pos = []

    similarity = None

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
    result.similarity = sim
    return result
