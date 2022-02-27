from os.path import join

import cv2 as cv
import numpy as np
from cv2 import imshow, waitKey
from cv2.cv2 import imwrite


def pil2cv(image) -> np.ndarray:
    return cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)


def cv2pil(image: np.ndarray):
    pass


def test_img(img, print_pos=False, win_name='test'):
    imshow(win_name, img)

    def on_mouse_action(event, x, y, flags, param):
        print(x, y)

    if print_pos:
        cv.setMouseCallback(win_name, on_mouse_action)
    cv.waitKey()


def crop_img(img: np.ndarray, file_name=None, file_path='.'):
    if file_name is None:
        file_name = 'crop'

    class Data:
        first_click = None
        second_click = None
        index = 0

    def handle_image(xs, ys):
        print(xs, ys)
        imwrite(join(file_path, "%s_%d.png" % (file_name, Data.index)), img[ys[0]:ys[1], xs[0]:xs[1]])
        Data.index += 1

    def on_mouse_action(event, x, y, flags, param):
        if event != cv.EVENT_LBUTTONUP:
            return
        if Data.first_click is None:
            Data.first_click = (x, y)
        else:
            Data.second_click = (x, y)

            x1, y1 = Data.first_click
            x2, y2 = Data.second_click
            xs, ys = [x1, x2], [y1, y2]
            xs.sort()
            ys.sort()
            handle_image(xs, ys)

            Data.first_click = None
            Data.second_click = None

    win_name = 'crop'
    imshow(win_name, img)
    cv.setMouseCallback(win_name, on_mouse_action)
    waitKey()


def sim_screen_crop(solution: tuple, source: np.ndarray) -> np.ndarray:
    x, y = solution
    w, h, _ = source.shape

    scale = w / x
    dx, dy = int(x * scale), int(y * scale)

    center = (w // 2, h // 2)
    cx, cy = center
    # print(center)
    x1, y1 = cx - dx // 2, cy - dy // 2
    x2, y2 = cx + dx // 2, cy + dy // 2
    # p1, p2 = (x1, y1), (x2, y2)
    # print(p1, p2)
    return source[y1:y2, x1:x2]

