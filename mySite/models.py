from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Channel(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    profilePic = models.TextField()
    description = models.TextField()
    joinedDate = models.DateTimeField()
    totalViews = models.BigIntegerField()
    subscriberCount = models.TextField()
    videos =  ArrayField(models.TextField())

class Video(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    videoThumbnail = models.TextField()
    interactionCount = models.BigIntegerField()
    likeCount = models.BigIntegerField()
    dislikecount = models.BigIntegerField()
    uploadDate = models.DateTimeField()
    datePublished = models.DateTimeField()
    channelID = models.TextField()
    genre = models.TextField()
    comments = ArrayField(models.TextField())