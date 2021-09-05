from django.shortcuts import render

from .models import Channel
from .models import Video
# Create your views here.
def index(request):
    videos = Video.objects.all()[0:21]
    data = {
        'videos': videos
    }
    return render(request, 'index.html', data)