import logging
import os
from datetime import datetime
from enum import IntEnum, auto

from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.dc import *
from bot.tg.fsm.memory_storage import MemoryStorage
from goals.models import Goal, Category, BoardParticipant

from todolist.settings import TG_TOKEN

logger = logging.getLogger(__name__)


class StateEnum(IntEnum):
    CREATE_CATEGORY_SELECT = auto()
    CHOSEN_CATEGORY = auto()


class NewGoal(BaseModel):
    cat_id: int | None = None
    goal_title: str | None = None

    @property
    def is_completed(self) -> bool:
        return None not in [self.cat_id, self.goal_title]


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient(TG_TOKEN)
        self.storage = MemoryStorage()

    def handle_unverified_user(self, message: Message, tg_user: TgUser):
        code: str = self._generate_verification_code()
        tg_user.verification_code = code
        tg_user.save(update_fields=('verification_code',))
        self.tg_client.send_message(
            chat_id=message.chat.id,
            text=f'[verification_code] {tg_user.verification_code}'
        )

    def handle_goals_list(self, message: Message, tg_user: TgUser):
        resp_goals: list[str] = [
            f'#{goal.id} {goal.title}'
            for goal in Goal.objects.filter(user_id=tg_user.user_id).order_by('due_date')
        ]
        if resp_goals:
            self.tg_client.send_message(message.chat.id, '\n'.join(resp_goals))
        else:
            self.tg_client.send_message(message.chat.id, '[You have no goals]')

    def handle_goals_categories_list(self, message: Message, tg_user: TgUser):
        resp_categories: list[str] = [
            f'#{cat.id} {cat.title}'
            for cat in Category.object.filter(
                board__participants__user_id=tg_user.user_id,
                is_deleted=False
            )
        ]
        if resp_categories:
            self.tg_client.send_message(message.chat.id, 'Select category\n' + '\n'.join(resp_categories))
        else:
            self.tg_client.send_message(message.chat.id, '[You have no categories]')

    def handle_save_selected_category(self, message: Message, tg_user: TgUser):
        if message.text.isdigit():
            cat_id = int(message.text)
            if Category.objects.filter(
                    board__participants__user_id=tg_user.user_id,
                    board__participants__role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
                    is_deleted=False,
                    id=cat_id
            ).exists():
                self.storage.update_data(chat_id=message.chat.id, cat_id=cat_id)
                self.tg_client.send_message(message.chat.id, '[set title]')
                self.storage.set_state(message.chat.id, state=StateEnum.CREATE_CATEGORY_SELECT)
            else:
                self.tg_client.send_message(message.chat.id, '[category not found]')
        else:
            self.tg_client.send_message(message.chat.id, '[invalid category id]')

    def handle_save_new_category(self, message: Message, tg_user: TgUser):
        goal = NewGoal(**self.storage.get_data(tg_user.chat_id))
        goal.goal_title = message.text
        if goal.is_completed:
            Goal.objects.create(
                title=goal.goal_title,
                category_id=goal.cat_id,
                user_id=tg_user.user_id,
                due_date=datetime.now()
            )
            self.tg_client.send_message(message.chat.id, '[New goal created]')
        else:
            logger.debug(goal)
            self.tg_client.send_message(message.chat.id, '[Something went wrong]')

        self.storage.reset(tg_user.chat_id)

    def handle_verified_user(self, message: Message, tg_user: TgUser):

        if message.text == '/goals':
            self.handle_goals_list(message, tg_user)

        elif message.text == '/create':
            self.handle_goals_categories_list(message, tg_user)
            self.storage.set_state(message.chat.id, state=StateEnum.CHOSEN_CATEGORY)
            self.storage.set_data(message.chat.id, data=NewGoal().dict())

        elif message.text == '/cancel' and self.storage.get_state(tg_user.chat_id):
            self.storage.reset(tg_user.chat_id)
            self.tg_client.send_message(message.chat.id, '[canceled]')

        elif state := self.storage.get_state(tg_user.chat_id):
            match state:
                case StateEnum.CREATE_CATEGORY_SELECT:
                    self.handle_save_selected_category(message, tg_user)
                case StateEnum.CHOSEN_CATEGORY:
                    self.handle_save_new_category(message, tg_user)
                case _:
                    logger.debug('Invalid state %s', state)

        elif message.text.startswith('/'):
            self.tg_client.send_message(message.chat.id, '[unknown command]')

    def handle_message(self, message: Message):
        tg_user, _ = TgUser.objects.select_related('user').get_or_create(
            chat_id=message.chat.id,
            defaults={
                'username': message.from_.username
            }
        )
        if tg_user.user:
            # Verified user
            self.handle_verified_user(message=message, tg_user=tg_user)
        else:
            # New user
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
                self.handle_message(message=item.message)
