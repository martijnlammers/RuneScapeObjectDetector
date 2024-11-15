from detector import Detector
from image import Image


if __name__ == "__main__":
    detector = Detector() 

    if(not detector.loaded()):
        detector.create_engine()

    result = detector.predict(image)
    # LoadImages()
    # TrainModel()
    # ExportModel()
    # LoadModel()
    # LoadInput()
    # PreProcess()
    # DetectObject()
    # PostProcess()
    # OutputPrediction()