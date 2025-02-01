from dataclasses import dataclass

from signalbot import Context, Command, triggered

from bot import persistence

help_text = """
Powderbot nutzung:

!powderbot <command>
    status: display current status and configuration
    [resort]: Schneebericht von [resort]
    map: Karte mit Schneefall der nächsten 24h
"""


class PowderBot(Command):
    @triggered("!powderbot")
    async def handle(self, c: Context):
        await c.send("POWDER!")

    async def status(self):
        pass


@dataclass
class ChatConfiguration:
    id: str
    active: bool = True
    daily: bool = True
    alert: bool = False

    def __init__(self, id: str):
        self.id = id
        config: dict = persistence.retrieve(f"powderbot/{id}")
        self.active, self.daily, self.alert = config

    def store(self):
        config = {
            "id": self.id,
            "active": self.active,
            "daily": self.daily,
            "alert": self.alert,
        }
        persistence.store(f"powderbot/{id}", config)
