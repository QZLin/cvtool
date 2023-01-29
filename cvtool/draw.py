import threading
import cv2 as cv
import numpy as np

DEFAULT_SIZE = 5
DEFAULT_COLOR = (0, 0, 255)


def point(image, *p, group_mode=False, **kwargs):
    if group_mode:
        pass
    else:
        if len(p) % 2 != 0:
            raise ValueError
        for i in range(0, len(p), 2):
            x, y = p[i], p[i + 1]
            cv.circle(image, (x, y), DEFAULT_SIZE // 2, DEFAULT_COLOR, -1)


def points(image, points_):
    pass


def line(image, x1, y1, x2, y2):
    cv.line(image, (x1, y1), (x2, y2), DEFAULT_COLOR, DEFAULT_SIZE)


def text(image, content, position, scale):
    cv.putText(image, content, position, cv.FONT_HERSHEY_SIMPLEX, scale, DEFAULT_COLOR, DEFAULT_SIZE, cv.LINE_AA)


class SimpleVisualizer:
    def __init__(self, cv_img, exit_key='q'):
        self.cv_img = cv_img
        self.exit_key = exit_key

        self.thread = None
        self.running = False

    def start(self, exit_key, *n):
        while cv.waitKey(1) != exit_key:
            cv.imshow(self.__class__.__name__, self.cv_img)
        self.running = False

    def run(self):
        self.thread = threading.Thread(target=self.start, args=[ord(self.exit_key)])
        self.thread.daemon = True
        self.thread.start()
        self.running = True

    def update(self, cv_img):
        self.cv_img = cv_img

    def post_update(self, x):
        self.cv_img = x(self.cv_img)


def int_to_rgb(i):
    if i == 0:
        return 0, 0, 0
    hex_s = str(hex(i)).lstrip('0x')
    r, g, b = (int(hex_s[x:x + 1], 16) for x in (0, 2, 4))
    return r, g, b


def matrix2d_colorize(image, matrix: np.ndarray, value_range=None, color_range=None):
    if value_range is None:
        value_range = [0, 100]
    if color_range is None:
        color_range = [0, 16777215]  # 0xFFFFFF to int

    value_min, value_max = value_range
    color_min, color_max = color_range

    w, h = matrix.shape
    for x in range(w):
        for y in range(h):
            value = matrix[x, y]
            value_percentage = (value - value_min) / value_max
            color_int = color_min + int((color_max - color_min) * value_percentage)
            r, g, b = int_to_rgb(color_int)
            image[x, y, 0] = r
            image[x, y, 1] = g
            image[x, y, 2] = b
    return image

# pt = point
# ln = lines
