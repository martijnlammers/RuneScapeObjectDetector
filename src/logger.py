
class Logger:
    def __init__(self):
        pass

    def info(self, msg: str) -> None:
        print("[I]", msg)

    def warning(self, msg: str):
        print("[W]", msg)

    def error(self, msg: str):
        print("[E]", msg)
