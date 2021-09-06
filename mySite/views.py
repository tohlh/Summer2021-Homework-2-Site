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
    videos = Video.objects.all().order_by('-interactionCount')[offset:offset + videosPerPage]
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

def search_videos_result(request):
    searched = request.POST['searched']
    
    keywords = searched.split(' ')
    videoQuery = Q()
    for keyword in keywords:
        videoQuery = Q(videoQuery | Q(title__icontains=keyword))
        videoQuery = Q(videoQuery | Q(description__icontains=keyword))
        
    videos = Video.objects.filter(videoQuery).order_by('-datePublished')

    data = {
        'searched': searched,
        'videos': videos,
    }

    return render(request, 'search-result-videos.html', data)

def search_channels_result(request):
    searched = request.POST['searched']

    keywords = searched.split(' ')
    channelQuery = Q()
    for keyword in keywords:
        channelQuery = Q(channelQuery | Q(name__icontains=keyword))
        channelQuery = Q(channelQuery | Q(description__icontains=keyword))

    channels = Channel.objects.filter(channelQuery)

    data = {
        'searched': searched,
        'channels': channels,
    }

    return render(request, 'search-result-channels.html', data)

def video_details(request, id):
    video = Video.objects.get(id = id)
    channel = Channel.objects.get(id = video.channelID)

    data = {
        'video': video,
        'channel': channel,
    }

    return render(request, 'video-details.html', data)

def channel_details(request, id):
    channel = Channel.objects.get(id=id)

    data = {
        'channel': channel,
    }

    return render(request, 'channel-details.html', data)