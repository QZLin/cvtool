import warnings

import cv2 as cv
from numpy import where

from cvtool.image import CVImage


class MatchResult:

    def __init__(self, matched=False, similarity=None, pos=None, pos_in_list=False):
        self.matched = matched
        self.pos = [] if pos is None else pos
        self.wrap_pos = pos_in_list

        self.similarity = similarity

    def __str__(self):
        return f"Result:{self.matched}&{self.pos}"


def match(source: CVImage, image: CVImage, similarity=0.85) -> MatchResult:
    """

    :param source:
    :param image:
    :param similarity:
    :return:
    """
    res = cv.matchTemplate(image, source, cv.TM_CCOEFF_NORMED)
    _, sim, min_loc, max_loc = cv.minMaxLoc(res)

    result = MatchResult(matched=sim > similarity, similarity=similarity)
    if result.matched:
        result.pos = max_loc
    return result


def match_all(source: CVImage, image: CVImage, similarity=0.85):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    source = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

    res = cv.matchTemplate(image, source, cv.TM_CCOEFF_NORMED)

    loc = where(res >= similarity)
    result = MatchResult()
    result.pos = []
    for pt in zip(*loc[::-1]):
        result.pos.append(pt)
        # w, h = image.shape[::-1]
        # cv.rectangle(source, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    result.wrap_pos = True
    if len(result.pos) > 0:
        result.matched = True
    # cv.imwrite('debug#match_all.png', source)
    return result


def remove_close_point(point_list, distance):
    warnings.warn("use remove_similar_vec instead", DeprecationWarning)
    raise RuntimeError("not implement")
