from detector import Detector
from image import Image
from config import Config

if __name__ == "__main__":

    config = Config('detector_config.json')
    frame = Image(config.frame_path)
    target = Image(config.target_path)

    detector = Detector(config.debug)
    detector.set_confidence(config.confidence)
    result = detector.locate(frame, target)
