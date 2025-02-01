from textwrap import dedent

from signalbot import Context, Command, regex_triggered

from powderbot.config import ChatConfiguration

help_text = """
Powderbot nutzung:

!powderbot <command>
    status: display current status and configuration
    [resort]: Schneebericht von [resort]
    map: Karte mit Schneefall der nächsten 24h
"""


class PowderBot(Command):
    context: Context = None
    config: ChatConfiguration = None

    @regex_triggered(r"^\!powder(bot)?")
    async def handle(self, c: Context):
        self.context = c
        self.config = ChatConfiguration(self.context.message.recipient())

        arguments = self.context.message.text.split()[1:]

        if len(arguments) == 0:
            await self.context.send(help_text)
            return

        command = arguments[0]

        match command:
            case "status":
                await self.status()
            case "activate":
                await self.activate()

        await c.send("POWDER!")

    async def status(self):
        text = dedent(f"""
            Powderbot status:
            active: {"✅" if self.config.active else "❌"}
            daily: {"✅" if self.config.daily else "❌"}  
            alert: {"✅" if self.config.alert else "❌"}
            
            id: {self.context.message.recipient()}
        """)

        await self.context.send(text)

    async def activate(self):
        self.config.active = True
        self.config.store()