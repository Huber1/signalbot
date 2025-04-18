import asyncio
import logging
import os

from signalbot import SignalBot, Command, Context, regex_triggered
from signalbot.storage import InMemoryStorage

from musicbot.message_handler import MessageHandler

logger = logging.getLogger(__name__)


class HandlePingMessage(Command):

    @regex_triggered("ping")
    async def handle(self, c: Context):
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

        await c.send("pong")


async def task(bot):
    await bot.send("11c515d6-b48c-42f7-9c91-97602dfe0a63", f"Bot started")


if __name__ == "__main__":
    bot = SignalBot({
        "signal_service": os.environ["SIGNAL_SERVICE"],
        "phone_number": os.environ["PHONE_NUMBER"],
    })
    bot.storage = InMemoryStorage()

    bot.register(HandlePingMessage())
    bot.register(MessageHandler(bot))

    loop = asyncio.get_event_loop()
    loop.create_task(task(bot))

    print("Starting Bot")

    bot.start()
