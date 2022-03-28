import argparse

import cv2 as cv
import numpy as np

from cvtool.image import CVImage


def merge(source: CVImage, alpha: CVImage):
    h, w, channel = source.shape
    b, g, r = cv.split(source)

    image = np.zeros((4, h, w), dtype=source.dtype)
    image[0][0:h, 0:w] = b
    image[1][0:h, 0:w] = g
    image[2][0:h, 0:w] = r
    image[3][0:h, 0:w] = alpha
    return cv.merge(image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str)
    parser.add_argument("alpha", type=str)
    parser.add_argument("output", type=str)
    args = parser.parse_args()

    source_img = cv.imread(args.source)
    alpha_img = cv.imread(args.alpha, 0)

    img = merge(source_img, alpha_img)
    cv.imwrite(args.output, img)
