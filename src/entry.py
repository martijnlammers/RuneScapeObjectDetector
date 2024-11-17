from detector import Detector
from image import Image

if __name__ == "__main__":

    detector = Detector() 
    import cv2 
    target = Image('res\\test.png')
    result = detector.locate(target)
    print(result)