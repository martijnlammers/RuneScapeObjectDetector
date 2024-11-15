
import Detector, Image, Logger


if __name__ == "__main__":
    detector = Detector() 
    logger = Logger()

    if(not detector.load()):
        logger.info("Could not load engine.")
    LoadImages()
    TrainModel()
    ExportModel()
    LoadModel()
    LoadInput()
    PreProcess()
    DetectObject()
    PostProcess()
    OutputPrediction()