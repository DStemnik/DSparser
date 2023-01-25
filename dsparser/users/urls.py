from django.urls import path, include
from django.views.generic import TemplateView
from .views import RegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='users/main.html'),
         name='user'),
    path('register/', RegisterView.as_view(), name='register'),

]