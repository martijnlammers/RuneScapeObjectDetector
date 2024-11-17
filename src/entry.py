from detector import Detector
from image import Image
from config import Config

if __name__ == "__main__":

    config = Config('detector_config.json')
    screenshot = Image(config.screenshot_path)
    target = Image(config.target_path)

    detector = Detector(config.debug)
    detector.set_confidence(config.confidence)
    result = detector.locate(screenshot, target)
