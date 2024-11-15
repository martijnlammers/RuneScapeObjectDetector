
class Logger:
    def __init__(self):
        pass

    def info(self, msg: str) -> None:
        print("[INFO] ", msg)

    def warning(self, msg: str):
        print("[WARNING] ", msg)

    def error(self, msg: str):
        print("[ERROR] ", msg)