from django.shortcuts import render

from .models import Channel
from .models import Video
# Create your views here.
def index(request):
    return render(request, 'index.html')