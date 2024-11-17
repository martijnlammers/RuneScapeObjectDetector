import cv2


class Image:

    name: str = "default"
    path: str = "default"
    data: cv2.typing.MatLike

    def __init__(self, path: str = 'None'):
        self.name = path.split('\\')[-1]
        self.path = path
        self.data = cv2.imread(path, cv2.IMREAD_COLOR)
