from django.shortcuts import render

from math import ceil
from .models import Channel
from .models import Video
# Create your views here.
def index(request, page=1):
    offset = (page - 1) * 21
    videos = Video.objects.all()[offset:offset + 21]
    maxLength = ceil(Video.objects.count() / 21)
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