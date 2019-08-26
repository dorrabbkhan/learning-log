"""
Forms file for Learning Log
"""

from django import forms
from .models import Topic

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
