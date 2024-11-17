# 3rd party
import cv2

# internal
import constants as const
from logging import info
from image import Image
from rectangle import Rectangle
from debug_functions import show_detection


class Detector:
    __confidence: float = const.DEFAULT_CONFIDENCE
    __debug: bool

    def __init__(self, debug: bool = False):
        self.__debug = debug

    def set_confidence(self, confidence: float) -> None:
        self.__confidence = confidence
        info(f"Detection confidence set to {self.__confidence}")

    def locate(self, frame: Image, target: Image, debug: bool = False) -> Rectangle:
        info(f"Locating {target.name} on {frame.name}")

        rectangle = None
        result = cv2.matchTemplate(frame.data, target.data, cv2.TM_CCOEFF_NORMED)
        confidence = cv2.minMaxLoc(result)[const.CONFIDENCE_INDEX]

        if (confidence >= self.__confidence):

            top_left = cv2.minMaxLoc(result)[const.TOP_LEFT_INDEX]

            rectangle = Rectangle(
                top_left[const.TOP_LEFT_X_INDEX],
                top_left[const.TOP_LEFT_Y_INDEX],
                target.data.shape[const.WIDTH_INDEX],
                target.data.shape[const.HEIGHT_INDEX]
            )

            info(f"Target found with confidence: {confidence}")

            if (self.__debug):
                show_detection(frame, rectangle)

        else:
            info("No match")

        return rectangle
