import numpy as np
import cv2
import matplotlib.pyplot as plt


def canny():
    img = cv2.imread("E:/dev/vsc_workspace/python/opencv/test2.jpg", cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 100, 100)
    cv2.imshow('edge1', edge1)
    cv2.waitKey(0)
    cv2.destoryAllWindows()


canny()
