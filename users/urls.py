"""
URL patterns for users application
"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # default auth urls
    path('register/', views.register, name='register')
]