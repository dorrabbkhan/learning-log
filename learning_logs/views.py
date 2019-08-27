from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    """
    Homepage for learning log
    """

    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """
    Topics page
    """

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    # define topics and context for the page

    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """
    Individual topic page
    """

    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    # make sure topic's owner is the one who requested it

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    # define topic, entries and context for webpage

    return render(request, 'learning_logs/topic.html', context)

@login_required
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
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
            # if form is valid, save and redirect

    context = {'form': form}
    # create context and return new blank form

    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """
    Create new entry
    """

    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    # create empty form if data is not submitted

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        # if form is valid, save entry and redirect to topic page

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """
    Edit an entry
    """

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # obtain entry and topic

    if topic.owner != request.user:
        raise Http404
    # make sure entry's owner is the one who requested it

    if request.method != 'POST':
        form = EntryForm(instance=entry)
        # prefill the form with existing entry
    
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        # submit form and save and redirect

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def del_entry(request, entry_id):
    """
    Delete an entry
    """

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # obtain entry and topic

    if topic.owner == request.user:
        Entry.objects.filter(id=entry_id).delete()
        return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        raise Http404
    # if user owns the topic, then delete the entry
    # and redirect, else raise 404 error

@login_required
def del_topic(request, topic_id):
    """
    Delete an entry
    """

    topic = Topic.objects.get(id=topic_id)
    # obtain topic

    if topic.owner == request.user:
        Topic.objects.filter(id=topic_id).delete()
        return redirect('learning_logs:topics')
    else:
        raise Http404
    # if user owns the topic, then delete the entry
    # and redirect, else raist 404 error