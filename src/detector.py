# 3rd party
import pyautogui as pg
import cv2
from pyautogui import ImageNotFoundException

# internal
from logger import Logger
from image import Image

# standard
from typing import Tuple

class Detector:

    __logger: Logger = Logger()

    def locate(s, target: Image) -> Tuple[int, int, int, int]:
        s.__logger.info("Attempting to locate image: " + target.name)

        try:
            result =  pg.locateOnScreen(target.path, confidence=0.7)
            s.__logger.info("Image found!")
            return result
        
        except ImageNotFoundException:
            s.__logger.error("Image not found on screen.")