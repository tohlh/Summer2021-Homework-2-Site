from django.contrib import admin

from .models import Channel
from .models import Video

admin.site.register(Channel)
admin.site.register(Video)