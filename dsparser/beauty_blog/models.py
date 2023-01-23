from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            on_delete=models.SET_NULL,
                            related_name='children', db_index=True,
                            verbose_name='Родительская категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    meta_description = models.TextField(blank=True,
                                        max_length=120,
                                        verbose_name='Мета-описание')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Содержание')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='ЧПУ')
    category = TreeManyToManyField(Category, related_name='cat_articles',
                                   verbose_name='Категория')
    main = models.BooleanField(default=False, verbose_name='Главная')
    meta_description = models.TextField(blank=True,
                                        max_length=120,
                                        verbose_name='Мета-описание')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


