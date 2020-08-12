from django.urls import path
from .views import articles_list, detail_article, new_article

urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('article/<int:pk>/', detail_article, name='detail_article'),
    path('article/new/', new_article, name='new_article'),
]