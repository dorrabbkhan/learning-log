"""
URL patterns for users application
"""

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
    # default auth urls
]