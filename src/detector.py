# 3rd party
import cv2

# internal
import constants as const
from logger import Logger
from image import Image

# standard library
from typing import dict


class Detector:

    __logger: Logger = Logger()
    __confidence: float = const.DEFAULT_CONFIDENCE
    __debug: bool

    def __init__(s, debug: bool = False):
        s.__debug = debug

    def set_confidence(s, confidence: float) -> None:
        s.__confidence = confidence
        s.__logger.info(f"Detection confidence set to {s.__confidence}")

    def locate(s, screenshot: Image, target: Image, debug: bool = False) -> dict[int, int, int, int]:
        s.__logger.info("Locating " + target.name + " on " + screenshot.name)

        match = None
        result = cv2.matchTemplate(screenshot.data, target.data, cv2.TM_CCOEFF_NORMED)
        confidence = cv2.minMaxLoc(result)[const.CONFIDENCE_INDEX]

        if (confidence >= s.__confidence):

            top_left = cv2.minMaxLoc(result)[const.TOP_LEFT_INDEX]
            match = {
                "left": top_left[const.TOP_LEFT_X_INDEX],
                "top": top_left[const.TOP_LEFT_Y_INDEX],
                "width": target.data.shape[const.WIDTH_INDEX],
                "height": target.data.shape[const.HEIGHT_INDEX]
                }

            s.__logger.info(f"Target found with confidence: {confidence}")
            s.__logger.info(f"Coordinates: {match}")

            if (s.__debug):
                s.__show_detection(screenshot, match)

        else:
            s.__logger.info("No match")

        return match

    def __show_detection(self, screenshot: Image, match: dict[int, int, int, int]):
        x = match['left']
        y = match['top']
        w = match['width']
        h = match['height']
        cv2.rectangle(screenshot.data, (x, y), (x + w, y + h), const.RGB_RED, 3)

        draw_point = (x, y - 10)
        font = cv2.FONT_HERSHEY_PLAIN
        font_scale = 0.8
        cv2.putText(screenshot.data, 'Detection', draw_point, font, font_scale, const.RGB_RED)
        cv2.imshow("Detection Verification", screenshot.data)
        cv2.waitKey()
