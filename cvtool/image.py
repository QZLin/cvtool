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


def crop_img(img: np.ndarray, file_name=None):
    if file_name is None:
        file_name = 'crop.png'

    class Data:
        first_click = None
        second_click = None

    def handle_image(xs, ys):
        print(xs, ys)
        imwrite(file_name, img[ys[0]:ys[1], xs[0]:xs[1]])

    def on_mouse_action(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONUP:
            # print(event, x, y)
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

    name = 'crop'
    imshow(name, img)
    cv.setMouseCallback(name, on_mouse_action)
    waitKey()
