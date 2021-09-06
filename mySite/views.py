from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Q

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
    if (page > maxLength):
        return HttpResponseNotFound('<h1>Page not found</h1>')
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
    if (page > maxLength):
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'channels.html', data)

def search_result(request):
    searched = request.POST['searched']

    keywords = searched.split(' ')

    videoQuery = Q()
    channelQuery = Q()
    for keyword in keywords:
        videoQuery = Q(videoQuery | Q(title__icontains=keyword))
        videoQuery = Q(videoQuery | Q(description__icontains=keyword))
        channelQuery = Q(channelQuery | Q(name__icontains=keyword))
        channelQuery = Q(channelQuery | Q(description__icontains=keyword))
    videos = Video.objects.filter(videoQuery).order_by('-datePublished')
    channels = Channel.objects.filter(channelQuery)

    data = {
        'searched': searched,
        'videos': videos,
        'channels': channels,
    }

    return render(request, 'search-result.html', data)