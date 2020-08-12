from django.urls import path
from .views import article_list, detail_article, new_article

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/<int:pk>/', detail_article, name='detail_article'),
    path('article/new/', new_article, name='new_article'),
]