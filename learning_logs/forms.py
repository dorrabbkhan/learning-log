"""
Forms file for Learning Log
"""

from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """
    Form for topic
    """

    class Meta:
        """
        Metadata for TopicForm
        """

        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """
    Class for the form to create a new entry
    """

    class Meta:
        """
        Metadata for entry form
        """

        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}