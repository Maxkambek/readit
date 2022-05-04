from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse

from .forms import CreateCommentForm
from .models import Category,Tag,Article,Comment


def home_view(request):
    articles = Article.objects.order_by('-id')[:10]

    context = {'object_list': articles}
    return render(request, 'articles/index.html', context)


def article_list_view(request):
    articles = Article.objects.order_by('-id')
    search=request.GET.get('q')
    category=request.GET.get('cat')
    if search:
        articles=articles.filter(title__icontains=search)
    if category:
        articles=articles.filter(category__title__exact=category)

    context = {'object_list': articles}

    return render(request, 'articles/articles.html', context)


def article_detail_view(request, slug):
    form = CreateCommentForm()
    article = get_object_or_404(Article, slug=slug)
    last_2_articles = Article.objects.order_by('-id')[:2]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(article__slug=slug).order_by('-id')

    if request.method == 'POST':
        form = CreateCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(f'/detail/{article.slug}#comments')

    context = {
        'object': article,
        'last_2_articles': last_2_articles,
        'categories': categories,
        'tags': tags,
        'comments': comments,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)



