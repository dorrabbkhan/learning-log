"""
URL patterns for learning_logs
"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    # homepage
    path('topics/', views.topics, name='topics'),
    # topics page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page for each topic
]
# app name and urls