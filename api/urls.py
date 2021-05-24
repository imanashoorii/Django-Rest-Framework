from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (list_article,
                    update_article,
                    ArticleView,
                    ArticleDetailView,
                    ArticleGenericView,
                    ArticleDetailGenericView,
                    UserListView,
                    UserDetailView
                    )

urlpatterns = [
    path('article/', list_article),
    path('article/<int:pk>', update_article),
    path('article/all/', ArticleView.as_view()),
    path('article/detail/<int:pk>/', ArticleDetailView.as_view()),
    path('article/generics/all', ArticleGenericView.as_view()),
    path('article/generics/detail/<int:pk>/', ArticleDetailGenericView.as_view()),
    path('users/all/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
