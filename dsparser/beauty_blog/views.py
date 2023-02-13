from django.shortcuts import render
from .models import Category, Article
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Article
    template_name = 'beauty_blog/index.html'
    context_object_name = 'articles'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'beauty_blog/category_detail.html'


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'beauty_blog/article_detail.html'

