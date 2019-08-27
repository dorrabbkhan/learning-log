from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """
    Class for Topic that user is learning about
    """

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # initialize fields

    def __str__(self):
        return self.text

class Entry(models.Model):
    """
    Class for user entries
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # initialize fields

    class Meta:
        # metadata for an entry
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...'