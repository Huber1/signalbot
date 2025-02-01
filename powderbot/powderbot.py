from signalbot import Context

from command_handler import CommandHandler


class PowderBotHandler(CommandHandler):
    def handle(self, c: Context, arguments: list[str]):
        c.reply("Hello There")
