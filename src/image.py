class Image:

    name: str = "default"
    path: str = "default"

    def __init__(s, path: str = 'None'):
        s.name = path.split('\\')[-1]
        s.path = path