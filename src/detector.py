# 3rd party
import cv2

# internal
import constants as const
from logger import Logger
from image import Image
from rectangle import Rectangle
from debug_functions import show_detection


class Detector:

    __logger: Logger = Logger()
    __confidence: float = const.DEFAULT_CONFIDENCE
    __debug: bool

    def __init__(s, debug: bool = False):
        s.__debug = debug

    def set_confidence(s, confidence: float) -> None:
        s.__confidence = confidence
        s.__logger.info(f"Detection confidence set to {s.__confidence}")

    def locate(s, screenshot: Image, target: Image, debug: bool = False) -> Rectangle:
        s.__logger.info("Locating " + target.name + " on " + screenshot.name)

        rectangle = None
        result = cv2.matchTemplate(screenshot.data, target.data, cv2.TM_CCOEFF_NORMED)
        confidence = cv2.minMaxLoc(result)[const.CONFIDENCE_INDEX]

        if (confidence >= s.__confidence):

            top_left = cv2.minMaxLoc(result)[const.TOP_LEFT_INDEX]

            rectangle = Rectangle(
                top_left[const.TOP_LEFT_X_INDEX],
                top_left[const.TOP_LEFT_Y_INDEX],
                target.data.shape[const.WIDTH_INDEX],
                target.data.shape[const.HEIGHT_INDEX]
            )

            s.__logger.info(f"Target found with confidence: {confidence}")

            if (s.__debug):
                show_detection(screenshot, rectangle)

        else:
            s.__logger.info("No match")

        return rectangle
