import cv2
import constants as const

from image import Image
from rectangle import Rectangle


def show_detection(frame: Image, rectangle: Rectangle):

    top_left = rectangle.top_left
    bottom_right = rectangle.bottom_right

    cv2.rectangle(frame.data, top_left, bottom_right, const.RGB_RED, const.BOX_THICKNESS)
    cv2.putText(frame.data, 'Detection', rectangle.bottom_right, const.FONT, const.FONT_SCALE, const.RGB_RED)
    cv2.imshow("Detection Verification", frame.data)
    cv2.waitKey()
