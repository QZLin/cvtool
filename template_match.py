import cv2 as cv


class MatchResult:
    matched = False
    pos = []

    similarity = None

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
