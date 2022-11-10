from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from bot.models import TgUser
from bot.serializers import TelegramUserSerializer
from bot.tg.client import TgClient
from todolist.settings import TG_TOKEN


class TelegramVerificationView(GenericAPIView):
    model = TgUser
    serializer_class = TelegramUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        s: TelegramUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data['tg_user']
        tg_user.user = self.request.user
        tg_user.save(update_fields=('user', ))

        instance_s: TelegramUserSerializer = self.get_serializer(tg_user)
        TgClient(TG_TOKEN).send_message(tg_user.chat_id, '[verification_was_successful]')
        return Response(instance_s.data)
