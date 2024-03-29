import itertools
from os.path import join

import cv2 as cv
import numpy as np

CVImage = np.ndarray
PILImage = None


def try_import_pillow():
    global PILImage
    if PILImage is None:
        try:
            from PIL import Image as PILImage
        except ModuleNotFoundError:
            raise RuntimeError("module PIL of Pillow not found")


def pil2cv(image: PILImage) -> CVImage:
    try_import_pillow()
    return cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)


def cv2pil(image: CVImage):
    try_import_pillow()
    PILImage.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))


def test_img(img, print_pos=False, win_name='test'):
    cv.imshow(win_name, img)

    def on_mouse_action(event, x, y, flags, param):
        print(x, y)

    if print_pos:
        cv.setMouseCallback(win_name, on_mouse_action)
    cv.waitKey()


def crop_image_tool(img: CVImage, file_name=None, file_path='.'):
    if file_name is None:
        file_name = 'crop'

    class Data:
        first_click = None
        second_click = None
        index = 0

    def handle_image(xs, ys):
        print(xs, ys)
        cv.imwrite(join(file_path, "%s_%d.png" % (file_name, Data.index)), img[ys[0]:ys[1], xs[0]:xs[1]])
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
    cv.imshow(win_name, img)
    cv.setMouseCallback(win_name, on_mouse_action)
    cv.waitKey()


def sim_screen_crop(solution: tuple, source: CVImage) -> CVImage:
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


def uimread(filename: str, flags=cv.IMREAD_UNCHANGED) -> CVImage:
    if filename.isascii():
        return cv.imread(filename, flags)
    else:
        with open(filename, "rb") as stream:
            array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        return cv.imdecode(array, flags)


def uimwrite(filename: str, ext: str, image: CVImage, *args):
    if filename.isascii():
        cv.imwrite(filename, image, *args)
    else:
        with open(filename, "wb") as stream:
            stream.write(cv.imencode(ext, image, *args)[1])


def empty_image(width, height, channel=3) -> CVImage:
    return np.zeros((width, height, channel), dtype=np.uint8)


def non_interpolation_scale(image: CVImage, value: int) -> CVImage:
    w, h, c = image.shape
    width, height = w * value, h * value
    result = empty_image(width, height, c)
    for iy, y_line in enumerate(image):
        for ix, point in enumerate(y_line):
            tx, ty = ix * value, iy * value
            for dx, dy in itertools.product(range(value), range(value)):
                result[ty + dy][tx + dx] = point

    return result
