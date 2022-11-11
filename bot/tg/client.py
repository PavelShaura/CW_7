import requests

from bot.tg.dc import GetUpdateResponse, SendMessageResponse


class TgClient:
    def __init__(self, token: str):
        self.token = token

    def get_url(self, method: str) -> str:
        return f"https://api.telegram.org/bot{self.token}/{method}"

    # def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdateResponse:
    #     url = self.get_url('getUpdates')
    #     response = requests.get(url, params={'offset': offset, 'timeout': timeout})
    #     return GetUpdateResponse(**response.json())

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdateResponse:
        url = self.get_url('getUpdates')

        params = {
            "offset": offset,
            "timeout": timeout
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Django application",
            "content-type": "application/json"
        }
        response = requests.get(url=url, headers=headers, params=params)

        return GetUpdateResponse(**response.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        url = self.get_url('sendMessage')
        response = requests.post(url, json={'chat_id': chat_id, 'text': text})
        return SendMessageResponse(**response.json())

