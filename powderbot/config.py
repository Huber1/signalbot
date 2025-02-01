import json
import os
import re
from os.path import exists


class ChatConfiguration:
    id: str
    daily: bool = False
    alert: bool = False

    def __init__(self, id: str):
        self.id = id

        if not exists(self.filename()):
            os.makedirs(os.path.dirname(self.filename()), exist_ok=True)
            return

        with open(self.filename(), "r") as file:
            config = json.loads(file.read())
            self.daily = config["daily"]
            self.alert = config["alert"]

    def store(self):
        config = {
            "id": self.id,
            "daily": self.daily,
            "alert": self.alert,
        }
        print(config)
        with open(self.filename(), "w") as file:
            file.write(json.dumps(config, indent=2))

    def filename(self):
        return "/persistent/powderbot/" + re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F=]", "-", self.id) + ".json"
