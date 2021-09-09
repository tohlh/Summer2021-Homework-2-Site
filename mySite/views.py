from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404
from django.db.models import Q
import timeit

from math import ceil
from .models import Channel
from .models import Video
# Create your views here.
def index(request, page=1):
    videosPerPage = 20
    maxLength = ceil(Video.objects.count() / videosPerPage)
    if (page > maxLength):
        data = {
            'error': 'Whoops! This page does not exist!'
        }      
        return render(request, 'error.html', data, status=404)

    offset = (page - 1) * videosPerPage
    videos = Video.objects.all().order_by('-interactionCount')[offset:offset + videosPerPage]
    data = {
        'videos': videos,
        'page': int(page),
        'maxLength': maxLength,
        'totalVideos': Video.objects.count()
    }

    return render(request, 'videos.html', data)

def channels(request, page=1):
    channelsPerPage = 18
    maxLength = ceil(Channel.objects.count() / channelsPerPage)
    if (page > maxLength):
        data = {
            'error': 'Whoops! This page does not exist!'
        }      
        return render(request, 'error.html', data, status=404)
    
    offset = (page - 1) * channelsPerPage
    channels = Channel.objects.all().order_by('-totalViews')[offset:offset + channelsPerPage]
    data = {
        'channels': channels,
        'page': int(page),
        'maxLength': maxLength,
        'totalChannels': Channel.objects.count()
    }

    return render(request, 'channels.html', data)

def search_videos_result(request, page=1):
    if request.method != 'POST':
        return redirect('/')

    searched = request.POST['searched']

    if searched != '':
        videoQuery = Q(title__icontains=searched)
        videoQuery = Q(videoQuery | Q(description__icontains=searched))
        ticks = timeit.default_timer()
        totalVideos = Video.objects.filter(videoQuery).order_by('-datePublished')
        timeUsed = timeit.default_timer()  - ticks

        videosPerPage = 20
        offset = (page - 1) * videosPerPage
        maxLength = ceil(totalVideos.count() / videosPerPage)
        videos = totalVideos[offset : offset + videosPerPage]

        data = {
            'searched': searched,
            'videos': videos,
            'page': page,
            'maxLength': maxLength,
            'totalVideos': totalVideos.count(),
            'timeUsed': round(timeUsed, 5),
        }
        return render(request, 'search-result-videos.html', data)

    else:
        data = {
            'searched': searched,
            'videos': None,
            'page': 0,
            'maxLength': 0,
            'totalVideos': 0,
            'timeUsed': 0,
        }
        return render(request, 'search-result-videos.html', data)

def search_channels_result(request, page=1):
    if request.method != 'POST':
        return redirect('/channels')

    searched = request.POST['searched']

    if searched != '':
        channelQuery = Q(name__icontains=searched)
        channelQuery = Q(channelQuery | Q(description__icontains=searched))

        ticks = timeit.default_timer()
        totalChannels = Channel.objects.filter(channelQuery)
        timeUsed = timeit.default_timer() - ticks

        channelsPerPage = 18
        offset = (page - 1) * channelsPerPage
        maxLength = ceil(totalChannels.count() / channelsPerPage)
        channels = totalChannels[offset : offset + channelsPerPage]

        data = {
            'searched': searched,
            'channels': channels,
            'page': page,
            'maxLength': maxLength,
            'totalChannels': totalChannels.count(),
            'timeUsed': round(timeUsed, 5),
        }

        return render(request, 'search-result-channels.html', data)
    else:
        data = {
            'searched': searched,
            'channels': None,
            'page': 0,
            'maxLength': 0,
            'totalChannels': 0,
            'timeUsed': 0,
        }

        return render(request, 'search-result-channels.html', data)

def video_details(request, id):
    try:
        video = Video.objects.get(id = id)
    except:
        data = {
            'error': 'Whoops! This page does not exist!'
        }      
        return render(request, 'error.html', data, status=404)

    channel = Channel.objects.get(id = video.channelID)

    data = {
        'video': video,
        'channel': channel,
    }
    
    return render(request, 'video-details.html', data)

def channel_details(request, id):
    try:
        channel = Channel.objects.get(id=id)
    except:
        data = {
            'error': 'Whoops! This page does not exist!'
        }      
        return render(request, 'error.html', data, status=404)

    videos = Video.objects.filter(channelID=channel.id).order_by('-interactionCount')

    data = {
        'channel': channel,
        'videos': videos,
    }
    
    return render(request, 'channel-details.html', data)

def handleError404(request, exception):
    data = {
        'error': 'Whoops! This page does not exist!'
    }

    return render(request, 'error.html', data, status=404)

def handleError403(request, exception):
    data = {
        'error': 'Forbidden!'
    }

    return render(request, 'error.html', data, status=403)

def handleError400(request, exception):
    data = {
        'error': 'Please try again!'
    }

    return render(request, 'error.html', status=400)

def handleError500(request):
    data = {
        'error': 'Internal server error!'
    }

    return render(request, 'error.html', status=500)