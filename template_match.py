import cv2 as cv
from numpy import where


class MatchResult:

    def __init__(self):
        self.matched = False
        self.pos = []
        self.pos_in_list = False

        self.similarity = None

    def __str__(self):
        return "Result:%s&%s" % (self.matched, self.pos)


def match(source, image, similarity=0.85):
    res = cv.matchTemplate(image, source, cv.TM_CCOEFF_NORMED)
    _, sim, min_loc, max_loc = cv.minMaxLoc(res)

    result = MatchResult()
    if sim > similarity:
        result.matched = True
        result.pos = max_loc
    result.similarity = sim
    return result


def match_all(source, image, similarity=0.85):
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

    result.pos_in_list = True
    if len(result.pos) > 0:
        result.matched = True
    # cv.imwrite('debug#match_all.png', source)
    return result


def remove_close_point(point_list, distance):
    """
    attention! length of all point must be same
    """
    points = point_list.copy()
    for point in points:
        others = points.copy()
        others.remove(point)
        for point_o in others:
            length = len(point)
            for i in range(len(point)):
                if abs(point[i] - point_o[i]) <= distance:
                    length -= 1
            if length == 0:
                points.remove(point)
                break

    return points


def rm_cpt(points, distance):
    remove_close_point(points, distance)
