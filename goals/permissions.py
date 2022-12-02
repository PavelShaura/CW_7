from rest_framework import permissions

from goals.models import BoardParticipant


class BasePermissionMixin(permissions.IsAuthenticated):
    roles = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(
                user=request.user,
                board=obj
            ).exists()

        return BoardParticipant.objects.filter(
            user=request.user,
            board=obj,
            role__in=self.roles
        ).exists()


class BoardPermissions(BasePermissionMixin):
    roles = [BoardParticipant.Role.owner]

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj)


class CategoryPermissions(BasePermissionMixin):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj.board)


class GoalPermissions(BasePermissionMixin):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj=obj.category.board)


class CommentPermissions(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
