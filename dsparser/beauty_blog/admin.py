from django.contrib import admin
from django import forms
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(),
                                  label='Описание')

    class Meta:
        model = Article
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    fields = ['title', 'slug', 'meta_description', 'description', 'category',
              'main']


admin.site.register(Article, PostAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
