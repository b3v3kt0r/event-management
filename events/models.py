from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="events")

    def __str__(self):
        return self.title
