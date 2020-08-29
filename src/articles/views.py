from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import ArticleForm, CommentForm
from .models import Article, Comments, Favourite


# Create your views here.

def index(request):
    articles_list = Article.objects.order_by("-pub_date")
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
    comments_list = Comments.objects.filter(article=article)
    if request.user.is_authenticated:
        favourite, created = Favourite.objects.get_or_create(article=article, author=request.user)
    else:
        favourite = None
    if request.method == 'POST':
        newComment = Comments(article=article, author=request.user, pub_date=timezone.now())
        form = CommentForm(request.POST, instance=newComment)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles:detail', args=(article.id,)))
    else:
        form = CommentForm()
    context = {'article': article,
               'form': form, 'comments_list':
                   comments_list, 'favourite': favourite}
    return render(request, 'articles/detail.html', context)


def profile(request):
    articles_list = Article.objects.filter(author=request.user)
    comments_list = Comments.objects.filter(author=request.user)
    liked_list = Favourite.objects.filter(author=request.user, liked=True)
    context = {'articles_list': articles_list,
               'comments_list': comments_list,
               'liked_list': liked_list,
               }
    return render(request, 'articles/profile.html', context)


def article_create_view(request):
    new_article = Article(author=request.user, pub_date=timezone.now())
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=new_article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})


def article_delete_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect(reverse('articles:index'))


def article_edit_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles:detail', args=(article.id,)))
    else:
        form = ArticleForm(instance=article)
    return render(request, "articles/edit_article.html",  {'form': form})


def article_like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    favourite, created = Favourite.objects.get_or_create(article=article, author=request.user)
    favourite.liked = not favourite.liked
    favourite.save()
    article.count()
    article.save()
    return redirect(reverse('articles:detail', args=(article.id,)))

