import json


class Config:

    target_path: str = ""
    screenshot_path: str = ""
    confidence: float = 0.9
    debug: bool = False

    def __init__(self, path: str):
        with open(path, 'r') as config_file:
            json_data = json.load(config_file)
            self.target_path = json_data['target_path']
            self.screenshot_path = json_data['screenshot_path']
            self.confidence = json_data['confidence']
            self.debug = json_data['debug']
