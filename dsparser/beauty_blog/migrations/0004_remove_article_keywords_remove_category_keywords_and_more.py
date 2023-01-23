# Generated by Django 4.1.5 on 2023-01-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty_blog', '0003_article_keywords_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='keywords',
        ),
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(blank=True, max_length=120, verbose_name='Мета-описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, max_length=120, verbose_name='Мета-описание'),
        ),
    ]