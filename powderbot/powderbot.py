from textwrap import dedent

from signalbot import Context, Command, regex_triggered

from powderbot.config import ChatConfiguration

help_text = """
Powderbot nutzung:

!powderbot <command>
    status: display current status and configuration
    [resort]: Schneebericht von [resort]
    map: Karte mit Schneefall der nächsten 24h
    daily [on|off]: Täglicher Schneebericht
    alert: [on|off]: Meldung bei viel Schneefall
"""


class PowderBot(Command):
    context: Context = None
    config: ChatConfiguration = None

    @regex_triggered(r"^\!powderbot")
    async def handle(self, c: Context):
        self.context = c
        self.config = ChatConfiguration(self.context.message.recipient())

        arguments = self.context.message.text.split()[1:]

        if len(arguments) == 0:
            await self.context.send(help_text)
            return

        command = arguments[0]

        match command.lower():
            case "status":
                await self.status()
            case "daily":
                await self.daily(arguments[1:])
            case "alert":
                await self.alert(arguments[1:])

        await c.send("POWDER!")

    async def status(self):
        text = dedent(f"""
            Powderbot status:
            active: {"✅" if self.config.active else "❌"}
            daily: {"✅" if self.config.daily else "❌"}  
            alert: {"✅" if self.config.alert else "❌"}
            
            id: {self.context.message.recipient()}
        """).strip()

        await self.context.send(text)

    async def daily(self, args: list[str]):
        if len(args) == 0:
            await self.context.send(help_text)
            return

        value = args[0]
        if value.lower() == "on":
            self.config.daily = True
            self.config.store()
            await self.context.send("Täglicher Bericht **eingeschaltet**", text_mode="styled")
        elif value.lower() == "off":
            self.config.daily = False
            self.config.store()
            await self.context.send("Täglicher Bericht **ausgeschaltet**", text_mode="styled")
        else:
            await self.context.send(help_text)

    async def alert(self, args: list[str]):
        if len(args) == 0:
            await self.context.send(help_text)
            return

        value = args[0]
        if value.lower() == "on":
            self.config.alert = True
            self.config.store()
            await self.context.send("Schneewarnung **eingeschaltet**", text_mode="styled")
        elif value.lower() == "off":
            self.config.alert = False
            self.config.store()
            await self.context.send("Schneewarnung **ausgeschaltet**", text_mode="styled")
        else:
            await self.context.send(help_text)
