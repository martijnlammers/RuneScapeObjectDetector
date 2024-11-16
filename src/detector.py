# 3rd party
from super_gradients.training import models
import torch

# internal
from logger import Logger
from image import Image

class Detector:

    __logger: Logger = Logger()
    __device: str
    __model_architecture: str
    __model: any

    def __init__(s):
        s.__device = 'cuda' if torch.cuda.is_available() else 'cpu'
        s.__model_architecture = 'yolo_nas_l'
        s.__model = models.get(s.__model_architecture, pretrained_weights="coco").to(s.__device)
        s.__model.eval()


    # def __load_configuration(s) -> bool:
    #     s.__logger.info("Loading configurations.")
    #     return False
    
    # def __load_annotations(s) -> bool:
    #     data_dir = "../datasets/cheetah"

    # def __train(s) -> bool:
    #     s.__logger.info("Training model for object detection.")
    #     s.__load_annotations()

    
    # def __evaluate(s) -> None:
    #     s.__logger.info("Evaluating model to verify training.")

    def infer(s, image: Image) -> None:
        s.__logger.info("Performing inference on image: " + image.name)
        
