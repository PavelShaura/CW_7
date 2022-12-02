from rest_framework import serializers

from goals.models import Goal, BoardParticipant
from core.serializers import RetrieveUpdateSerializer


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "description", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted category")

        user = value.board.participants.filter(user=self.context["request"].user).first()
        if not user:
            raise serializers.ValidationError("not owner or writer in the related board")
        elif user.role not in [BoardParticipant.Role.owner, BoardParticipant.Role.writer]:
            raise serializers.ValidationError("not owner or writer in the related board")

        return value


class GoalSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user", "category", "description")