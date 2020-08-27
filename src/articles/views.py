from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import ArticleForm
from .models import Article


# Create your views here.
def index(request):
    articles_list = Article.objects.order_by('id')
    context = {
        'articles_list': articles_list,
    }
    return render(request, 'articles/index.html', context)


def search(request):
    articles_list = Article.objects.filter(
        title__icontains=request.POST['condition']
    )
    context = {
        'articles_list': articles_list,
    }
    return render(request, 'articles/search_result.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})


def profile(request):
    print(request.user.username)
    article_list = Article.objects.filter(author=request.user.username)
    return render(request, 'articles/profile.html', {'article_list': article_list})


def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            newPost = Article(title=title, content=content,
                           author=request.user.username, pub_date=timezone.now()
                           )
            newPost.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})


def article_delete_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return HttpResponseRedirect(reverse('articles:index'))


def article_edit_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/edit_article.html", {'article': article})


def article_update_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.pub_date = timezone.now()
    article.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(article.id,)))

