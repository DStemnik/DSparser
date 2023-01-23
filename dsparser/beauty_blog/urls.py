from django.urls import path
from .views import (CategoryDetailView,
                    ArticleDetailView,
                    IndexView,)


urlpatterns = [
    path('<slug:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('posts/<slug:slug>',
         ArticleDetailView.as_view(), name='article_detail'),
    path('', IndexView.as_view(), name='index_view'),
]