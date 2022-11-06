from django.urls import path
import goals.views as views

urlpatterns = [
    path("goal_category/create", views.CategoryCreateView.as_view()),
    path("goal_category/list", views.CategoryListView.as_view()),
    path("goal_category/<pk>", views.CategoryView.as_view()),
    path("goal/create", views.GoalCreateView.as_view()),
    path("goal/list", views.GoalListView.as_view()),
    path("goal/<pk>", views.GoalView.as_view()),
    path("goal_comment/create", views.CommentCreateView.as_view()),
    path("goal_comment/list", views.CommentListView.as_view()),
    path("goal_comment/<pk>", views.CommentView.as_view()),
    path("board/create", views.BoardCreateView.as_view()),
    path("board/list", views.BoardListView.as_view()),
    path("board/<pk>", views.BoardView.as_view()),

]