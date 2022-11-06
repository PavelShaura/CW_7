from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from goals.models import Goal
from goals.serializers import GoalCreateSerializer, GoalSerializer
from goals.filters import GoalDateFilter
from goals.permissions import GoalPermissions


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created", "priority", "due_date"]
    ordering = ["-priority", "due_date", "title"]
    filterset_class = GoalDateFilter
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Goal.objects.filter(
            category__board__participants__user=self.request.user,
            is_deleted=False
        )


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [GoalPermissions]

    def get_queryset(self):
        return Goal.objects.filter(
            category__board__participants__user=self.request.user,
            is_deleted=False
        )

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance
