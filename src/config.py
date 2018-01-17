import json
def load_config(path="./config.json"):
    """Loads the config from `path`"""
    with open(path, "r") as f:
        return json.loads(f.read())
