# 3rd party
import cv2 
import numpy as np 

# internal
from logger import Logger
from image import Image

# standard library
from typing import Tuple

class Detector:

    __logger: Logger = Logger()
    __confidence: float = 0.9

    def set_confidence(s, confidence: float) -> None:
        s.__confidence = confidence
        s.__logger.info("Detection confidence set to " + str(s.__confidence))

    def locate(s, screenshot: Image, target: Image) -> Tuple[int, int, int, int]:
        s.__logger.info("Attempting to locate image " + target.name)

        match_result = cv2.matchTemplate(screenshot.data, target.data, cv2.TM_CCOEFF_NORMED) 

        confidence = cv2.minMaxLoc(match_result)[1]
        top_left = cv2.minMaxLoc(match_result)[3]

        if(confidence >= s.__confidence):
            s.__logger.info("Target found with confidence: " + str(confidence))
            result = (top_left[0], top_left[1], target.data.shape[1], target.data.shape[0])
            return result
        
        # if max_val >= 0.8:
        #     top_left = max_loc 
        #     bottom_right = (top_left[0] + target_width, top_left[1] + target_height) 
        #     retval =  (top_left, bottom_right) 
        #     print(retval)
        # else:
        return None
   