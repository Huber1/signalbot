from signalbot import Context

from command_handler import CommandHandler


class PowderBotHandler(CommandHandler):
    async def handle(self, c: Context, arguments: list[str]):
        await c.reply("Hello There")
