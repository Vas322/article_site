from django.contrib import admin
from blog.models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    """Displaying an article in the admin panel"""
    fieldsets = [
        ('Введите название статьи', {'fields': ['title']}),
        ('Введите текст статьи', {'fields': ['text'[:20]]}),
        ('Информация о дате создания статьи', {'fields': ['created_date']}),
        ('Выберите изображение статьи', {'fields': ['image']}),
    ]
    list_display = ('title', 'created_date')


admin.site.register(Article, ArticleAdmin)
