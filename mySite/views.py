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

def channels(request):
    channels = Channel.objects.all()
    data = {
        'channels': channels
    }
    return render(request, 'channels.html', data)