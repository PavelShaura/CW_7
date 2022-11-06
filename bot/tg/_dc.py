from dataclasses import field
from typing import List, Optional

from marshmallow_dataclass import dataclass
from marshmallow import EXCLUDE


@dataclass
class MessageFrom:
    """Telegram API: https://core.telegram.org/bots/api#user"""
    id: int
    first_name: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class Chat:
    """Telegram API: https://core.telegram.org/bots/api#chat"""
    id: int
    type: str
    first_name: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    """Telegram API: https://core.telegram.org/bots/api#message"""
    message_id: int
    chat: Chat
    # override usage of keyword "from" - add underscore and metadata to map to data key
    from_: Optional[MessageFrom] = field(metadata=dict(data_key='from'), default=None)
    text: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    """Telegram API: https://core.telegram.org/bots/api#getting-updates"""
    update_id: int
    message: Optional[Message] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    """https://core.telegram.org/bots/api#getupdates"""
    ok: bool
    result: List[UpdateObj]

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    """https://core.telegram.org/bots/api#sendmessage"""
    ok: bool
    result: Message

    class Meta:
        unknown = EXCLUDE
