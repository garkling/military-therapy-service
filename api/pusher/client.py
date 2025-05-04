from enum import StrEnum

import pusher

from api.config import conf


class ChatEvents(StrEnum):
    MESSAGE_CREATED = "MESSAGE_CREATED"


class PusherClient:

    def __init__(self):
        self._client = pusher.Pusher(
            app_id=conf.PUSHER_APP_ID,
            key=conf.PUSHER_KEY,
            secret=conf.PUSHER_SECRET,
            cluster=conf.PUSHER_CLUSTER,
            ssl=True,
        )

    def send(self, room_id: str, data: dict):
        self._client.trigger(
            channels=[room_id],
            event_name=ChatEvents.MESSAGE_CREATED,
            data=data
        )
