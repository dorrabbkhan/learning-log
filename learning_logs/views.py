from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

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

def new_topic(request):
    """
    Add new topic
    """

    if request.method != "POST":
        form = TopicForm()
        # if data not submitted, create blank form
    else:
        form = TopicForm(data=request.POST)
        # submit POST data

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
            # if form is valid, save and redirect

    context = {'form': form}
    # create context and return new blank form
    
    return render(request, 'learning_logs/new_topic.html', context)

