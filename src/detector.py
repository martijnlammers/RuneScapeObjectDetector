# 3rd party
import pyautogui as pg
from pyautogui import ImageNotFoundException

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

    def locate(s, target: Image) -> Tuple[int, int, int, int]:
        s.__logger.info("Attempting to locate image " + target.name)

        try:
            result =  pg.locateOnScreen(target.path, confidence=s.__confidence)
            s.__logger.info("Image found!")
            return result
        
        except ImageNotFoundException:
            s.__logger.error("Image not found on screen.")