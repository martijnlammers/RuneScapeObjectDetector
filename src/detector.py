# 3rd party
import cv2

# internal
import constants as const
from logger import Logger
from image import Image

# standard library
from typing import Dict, Tuple


class Detector:

    __logger: Logger = Logger()
    __confidence: float = const.DEFAULT_CONFIDENCE
    __debug: bool

    def __init__(s, debug: bool = False):
        s.__debug = debug

    def set_confidence(s, confidence: float) -> None:
        s.__confidence = confidence
        s.__logger.info(f"Detection confidence set to {s.__confidence}")

    def locate(s, screenshot: Image, target: Image, debug: bool = False) -> Dict[str, int]:
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
        cv2.rectangle(screenshot.data, (x, y), (x + w, y + h), const.RGB_RED, 2)

        draw_point = (x, y - 10)
        font = cv2.FONT_HERSHEY_PLAIN
        font_scale = 0.8
        cv2.putText(screenshot.data, 'Detection', draw_point, font, font_scale, const.RGB_RED)
        cv2.imshow("Detection Verification", screenshot.data)
        cv2.waitKey()

    def locate_center(s, screenshot: Image, target: Image) -> Tuple[int, int] | None:
        """
        This method returns the center coordinates of located match rectangle.
        """
        locate_result = s.locate(screenshot, target)
        if locate_result is None:
            return None

        min_x, min_y, max_x, max_y = locate_result
        assert min_x <= max_x
        assert min_y <= max_y

        return (min_x + max_x) // 2, (min_y + max_y) // 2
