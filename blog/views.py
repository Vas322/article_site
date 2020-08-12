from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Article
from .forms import ArticleForm


def articles_list(request):
    """Controller that displays a list of 10 most recent articles"""
    art_last = Article.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')[:1]
    art_list = Article.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')[1:10]
    context = {'art_list': art_list, 'art_last': art_last}
    return render(request, "blog/article_list.html", context)


def detail_article(request, pk):
    """The controller displays detailed information about the article"""
    art = get_object_or_404(Article, pk=pk)
    context = {'art': art}
    return render(request, 'blog/detail_article.html', context)


def new_article(request):
    """Controller for creating a new article"""
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
