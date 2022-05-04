from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class ArticleManager(models.Manager):

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(title__icontains=query)
        obj = Article.objects.filter(lookup)
        return obj


class Category(models.Model):
    title=models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag=models.CharField(max_length=122)

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='articles')
    slug = models.SlugField()
    tag=models.ManyToManyField(Tag,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects=ArticleManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='articles/comment_author',null=True,blank=True)
    email=models.EmailField()
    website=models.URLField(null=True,blank=True)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
