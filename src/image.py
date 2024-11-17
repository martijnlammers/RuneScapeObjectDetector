import cv2 

class Image:

    name: str = "default"
    path: str = "default"
    data: cv2.typing.MatLike

    def __init__(s, path: str = 'None'):
        s.name = path.split('\\')[-1]
        s.path = path
        s.data = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 