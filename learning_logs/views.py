from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """
    Homepage for learning log
    """

    return render(request, 'learning_logs/index.html')

def topics(request):
    """
    Topics page
    """

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    # define topics and context for the page

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """
    Individual topic page
    """

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    # define topic, entries and context for webpage

    return render(request, 'learning_logs/topic.html', context)
