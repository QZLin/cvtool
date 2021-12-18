from os.path import join

import numpy as np
import cv2 as cv
from cv2 import imshow, waitKey
from cv2.cv2 import imwrite


def pil2cv(image) -> np.ndarray:
    return cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)


def cv2pil(image: np.ndarray):
    pass


def test_img(img, print_pos=False):
    win_name = 'test'
    imshow(win_name, img)

    def on_mouse_action(event, x, y, flags, param):
        if print_pos:
            print(x, y)

    cv.setMouseCallback(win_name, on_mouse_action)
    waitKey()


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
