# 3rd party
import cv2 

# internal
from logger import Logger
from image import Image
import constants as const

# standard library
from typing import Tuple

class Detector:

    __logger: Logger = Logger()
    __confidence: float = 0.9
    
    def set_confidence(s, confidence: float) -> None:
        s.__confidence = confidence
        s.__logger.info(f"Detection confidence set to {s.__confidence}")

    def locate(s, screenshot: Image, target: Image) -> Tuple[int, int, int, int] | None:
        s.__logger.info(f"Locating {target.name} on {screenshot.name}")

        match = None
        result = cv2.matchTemplate(screenshot.data, target.data, cv2.TM_CCOEFF_NORMED) 
        confidence = cv2.minMaxLoc(result)[const.CONFIDENCE_INDEX]

        if(confidence >= s.__confidence):

            top_left = cv2.minMaxLoc(result)[const.TOP_LEFT_INDEX]
            match = {
                "left": top_left[const.TOP_LEFT_X],
                "top": top_left[const.TOP_LEFT_Y],
                "width": target.data.shape[const.WIDTH],
                "height": target.data.shape[const.HEIGHT]
                }
            
            s.__logger.info(f"Target found with confidence: {confidence}")
            s.__logger.info(f"Coordinates: {match}")

        else:
            s.__logger.info("No match")
            
        return match
   