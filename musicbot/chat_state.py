from enum import Enum


class State(Enum):
    READY = 1
    WAITING_ALREADY_EXISTS = 2
    WAITING_SELECT_SONG = 3


class ChatState:
    state = State.READY
    messages: dict[str] = {}
    accepts: bool = True
