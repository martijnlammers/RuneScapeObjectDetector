from detector import Detector
from image import Image
from config import Config

if __name__ == "__main__":

    config = Config('detector_config.json')
    detector = Detector() 
    target = Image('res\\test.png')

    detector.set_confidence(config.confidence)
    result = detector.locate(target)
    print(result)