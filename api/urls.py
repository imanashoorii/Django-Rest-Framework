from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import list_article, update_article, ArticleView, ArticleDetailView

urlpatterns = [
    path('article/', list_article),
    path('article/<int:pk>', update_article),
    path('article/all/', ArticleView.as_view()),
    path('article/detail/<int:pk>/', ArticleDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)