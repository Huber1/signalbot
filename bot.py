import os

from signalbot import SignalBot, Command, Context

from command_handler import CommandHandler
from powderbot.powderbot import PowderBotHandler


class HandleMessage(Command):
    async def handle(self, c: Context):
        message = c.message.text
        command = message.split()[0]

        arguments = message.split()[1:]

        handler: CommandHandler | None = None

        print("MESSAGE INFO:")
        print(f"GROUP: {c.message.group}")
        print(f"SOURCE: {c.message.source}")
        print(f"TEXT: {c.message.text}")
        print(f"RAW_MESSAGE: {c.message.raw_message}")
        print(f"SOURCE_NUMBER: {c.message.source_number}")
        print(f"SOURCE_UUID: {c.message.source_uuid}")
        print(f"IS_PRIVATE: {c.message.is_private()}")
        print(f"IS_GROUP: {c.message.is_group()}")
        print(f"RECIPIENT: {c.message.recipient()}")

        match command.lower():
            case "!powderbot":
                handler = PowderBotHandler()

        if handler is not None:
            handler.handle(c, arguments)

        if c.message.text.lower() == "ping":
            await c.send("pong")


if __name__ == "__main__":
    bot = SignalBot({
        "signal_service": os.environ["SIGNAL_SERVICE"],
        "phone_number": os.environ["PHONE_NUMBER"],
    })
    bot.register(HandleMessage())
    bot.start()
