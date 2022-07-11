from django.contrib import admin

from songs.models import Album, Music

# Register your models here.
admin.site.register(Album)
admin.site.register(Music)