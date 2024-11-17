import cv2
import constants as const

from image import Image
from rectangle import Rectangle


def show_detection(self, frame: Image, rectangle: Rectangle):

    cv2.rectangle(frame.data, rectangle.top_left, rectangle.bottom_right, const.RGB_RED, const.BOX_THICKNESS)
    cv2.putText(frame.data, 'Detection', rectangle.bottom_right, const.FONT, const.FONT_SCALE, const.RGB_RED)
    cv2.imshow("Detection Verification", frame.data)
    cv2.waitKey()
