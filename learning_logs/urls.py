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
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding new topics
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # path for adding new entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # path for editing entry
    path('del_entry/<int:entry_id>/', views.del_entry, name='del_entry'),
    # path for deleting entry
    path('del_topic/<int:topic_id>/', views.del_topic, name='del_topic'),

]
# app name and urls