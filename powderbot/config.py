import re

from persistence_service import persistence


class ChatConfiguration:
    id: str
    active: bool = False
    daily: bool = True
    alert: bool = False

    def __init__(self, id: str):
        self.id = id
        config: dict = persistence.retrieve(f"powderbot/{self.clean_id()}")
        self.active, self.daily, self.alert = config

    def store(self):
        config = {
            "id": self.id,
            "active": self.active,
            "daily": self.daily,
            "alert": self.alert,
        }
        persistence.store(f"powderbot/{self.clean_id()}", config)

    def clean_id(self):
        return re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]=", "-", self.id)
