import cv2 as cv
import numpy

import cvtool as tool
from cvtool.image import CVImage

# You will get error with path contain unicode character
# cv.imread("example/asset/hdd-7880077_1280💽.jpg")
img: CVImage = tool.im.uimread("example/asset/hdd-7880077_1280💽.jpg")
tool.im.test_img(img)
