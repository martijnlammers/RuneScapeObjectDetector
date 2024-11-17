import json 

class Config:
    target_path: str = ""
    confidence: float = 0.9

    def __init__(s, path:str):
        with open(path, 'r') as config_file:
            json_data = json.load(config_file)
            target_path = json_data['target_path']
