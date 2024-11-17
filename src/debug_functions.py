import cv2
import constants as const

from image import Image
from rectangle import Rectangle


def show_detection(frame: Image, rectangle: Rectangle):

    cv2.rectangle(frame.data, rectangle.top_left(), rectangle.bottom_right(), const.RGB_RED, const.BOX_THICKNESS)

    top_left_point = rectangle.top_left()
    text_origin = (top_left_point[0], top_left_point[1] - 10)
    cv2.putText(frame.data, str(rectangle.top_left()), text_origin, const.FONT, const.FONT_SCALE, const.RGB_RED)
    cv2.imshow("Detection Verification", frame.data)
    cv2.waitKey()
