from rest_framework import serializers

from .models import TgUser


class TgUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = "__all__"
        read_only_fields = ("tg_user_id", "tg_chat_id")
