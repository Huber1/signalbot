import os

from signalbot import SignalBot, Command, Context


class PingCommand(Command):
    async def handle(self, c: Context):
        if c.message.text.lower() == "ping":
            await c.send("pong")


if __name__ == "__main__":
    bot = SignalBot({
        "signal_service": os.environ["SIGNAL_SERVICE"],
        "phone_number": os.environ["PHONE_NUMBER"],
    })
    bot.register(PingCommand())
    bot.start()
