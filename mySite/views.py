from django.shortcuts import render

from math import ceil
from .models import Channel
from .models import Video
# Create your views here.
def index(request, page=1):
    videosPerPage = 20
    offset = (page - 1) * videosPerPage
    videos = Video.objects.all()[offset:offset + videosPerPage]
    maxLength = ceil(Video.objects.count() / videosPerPage)
    data = {
        'videos': videos,
        'page': int(page),
        'maxLength': maxLength,
    }
    return render(request, 'index.html', data)

def channels(request, page=1):
    channelsPerPage = 18
    offset = (page - 1) * channelsPerPage
    channels = Channel.objects.all()[offset:offset + channelsPerPage]
    maxLength = ceil(Channel.objects.count() / channelsPerPage)
    data = {
        'channels': channels,
        'page': int(page),
        'maxLength': maxLength,
    }
    for channel in channels:
        print(channel.subscriberCount)

    return render(request, 'channels.html', data)