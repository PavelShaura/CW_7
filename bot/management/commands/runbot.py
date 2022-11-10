import os

from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.dc import Message

from todolist.settings import TG_TOKEN


class Command(BaseCommand):

    help = 'Implemented to Django application telegram bot setup command'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient(TG_TOKEN)

    def handle_unverified_user(self, message: Message, tg_user: TgUser):
        code: str = self._generate_verification_code()
        tg_user.verification_code = code
        tg_user.save(update_fields=('verification_code',))
        self.tg_client.send_message(
            chat_id=message.chat.id,
            text=f'[verification_code] {tg_user.verification_code}'
        )

    def handle_message(self, message: Message):
        tg_user, _ = TgUser.objects.select_related('user').get_or_create(
            chat_id=message.chat.id,
            defaults={
                'username': message.from_.username
            }
        )
        if tg_user.user:
            #Verified user
            self.tg_client.send_message(chat_id=message.chat.id, text='You have already verified')
        else:
            #New user
            self.handle_unverified_user(message=message, tg_user=tg_user)

    @staticmethod
    def _generate_verification_code() -> str:
        return os.urandom(12).hex()

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                # self.handle_message(message=item.message)
                # ehobot
                self.tg_client.send_message(chat_id=item.message.chat.id, text=item.message.text)
                print(item.message)
