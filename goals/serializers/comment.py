from rest_framework import serializers

from goals.models import Comment, BoardParticipant
from core.serializers import RetrieveUpdateSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"

    def validate_goal(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted goal")

        user = value.category.board.participants.filter(user=self.context["request"].user).first()
        if not user:
            raise serializers.ValidationError("not owner or writer of the related board")
        elif user.role not in [BoardParticipant.Role.owner, BoardParticipant.Role.writer]:
            raise serializers.ValidationError("not owner or writer of the related board")

        return value


class CommentSerializer(serializers.ModelSerializer):
    user = RetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")