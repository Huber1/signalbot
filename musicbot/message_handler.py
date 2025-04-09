from signalbot import Command, Context, SignalBot

from musicbot.chat_state import ChatState, State


class MessageHandler(Command):
    messages: dict[str, ChatState] = {}

    def __init__(self, bot: SignalBot):
        super().__init__()
        self.bot = bot

    async def handle(self, c: Context):
        if c.message.text.lower() == "ping": return;

        chat = self.messages[c.message.source]

        if not chat:
            chat = ChatState()

        match chat.state:
            case State.READY:
                await c.send("Downloading " + c.message.text)
            case State.WAITING_ALREADY_EXISTS:
                await c.send("Already exists")
            case State.WAITING_SELECT_SONG:
                await c.send("Select song")

        chat.state = State.READY
        self.messages[c.message.source] = chat
        return
