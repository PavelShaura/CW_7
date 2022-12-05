from pytest_factoryboy import register
from tests.factories import UserFactory, BoardFactory, CategoryFactory, GoalFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(BoardFactory)
register(CategoryFactory)
register(GoalFactory)
