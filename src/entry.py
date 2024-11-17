from detector import Detector
from image import Image

if __name__ == "__main__":

    detector = Detector() 
    target = Image('../res/test.png')
    result = detector.locate(target)
    print(result)