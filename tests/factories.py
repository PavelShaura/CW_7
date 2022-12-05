import factory

from core.models import User
from goals.models import Board, Category, Goal, Comment

from django.utils.timezone import now


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = "abcabc123123"


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = "test"
    is_deleted = False


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = "test"
    user = factory.SubFactory(UserFactory)
    is_deleted = False
    board = factory.SubFactory(BoardFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = "test"
    description = "test description"
    due_date = factory.LazyAttribute(lambda x: now())
    status = 2
    priority = 2
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    is_deleted = False


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    goal = factory.SubFactory(GoalFactory)
    text = 'test comment text'
