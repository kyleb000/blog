from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from datetime import datetime
import calendar


def get_timestamp():

    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    return unixtime


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title