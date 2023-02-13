from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            on_delete=models.SET_NULL,
                            related_name='children',
                            db_index=True,
                            verbose_name='Родительская категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    cover = models.ImageField(upload_to='images/', null=True, blank=True,
                              verbose_name='Обложка')

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
    category = TreeForeignKey(Category,
                              related_name='cat_articles',
                              verbose_name='Категория',
                              null=True,
                              on_delete=models.SET_NULL)
    main = models.BooleanField(default=False, verbose_name='Главная')
    cover = models.ImageField(upload_to='images/', null=True, blank=True,
                              verbose_name='Обложка')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def get_category(self):
        return ", ".join([str(p) for p in self.category.all()])

    get_category.short_description = 'Категория/и'


