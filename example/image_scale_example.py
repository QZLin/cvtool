import cv2 as cv
import cvtool as cvt

img = cv.imread('example/asset/opencv-logo.png')
result = cvt.im.int_scale(img, 4)
cvt.im.test_img(result)
cv.imwrite('test/result.png', result)
