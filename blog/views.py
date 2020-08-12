from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Article
from .forms import ArticleForm


def article_list(request):
    """Контроллер, который отображает список последних 10 статей"""
    articles_last = Article.objects.filter(created_date__lte=timezone.now()).order_by(
        '-created_date')[:10]
    context = {'articles_last': articles_last}
    return render(request, "blog/article_list.html", context)


def detail_article(request, pk):
    """Контроллер отображает детальную информацию о статье"""
    art = get_object_or_404(Article, pk=pk)
    context = {'art': art}
    return render(request, 'blog/detail_article.html', context)


def new_article(request):
    """Контроллер создания новой статьи"""
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save()
            messages.add_message(request, messages.SUCCESS, 'Статья добавлена!')
            return redirect('detail_article', pk=art.pk)
    else:
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'blog/new_article.html', context)
