from django.shortcuts import render
from .models import Category, Article
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Category
    context_object_name = 'cat'
    template_name = 'beauty_blog/index.html'
    extra_context = {
        'articles': Article.objects.filter(main=True)
    }


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'beauty_blog/category_detail.html'
    extra_context = {
        'cat': Category.objects.all()
    }


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'beauty_blog/article_detail.html'
    extra_context = {
        'cat': Category.objects.all()
    }
