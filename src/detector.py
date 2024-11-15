from logger import Logger

class Detector:

    __logger: Logger = Logger()
    __onnx_path: str = ""

    def __init__(self):
        self.__load_annotations()
        self.__train()
        self.__evaluate()

    def __load_annotations(self) -> bool:
        self.logger.info("Loading annotations for model training.")
        return False

    def __train(self) -> bool:
        self.logger.info("Training model for object detection.")
        self.__load_annotations()

    
    def __evaluate():
        self.logger.info("Evaluating model to verify training.")
