from django.shortcuts import render, redirect
from django.views import View
from .models import Artist,Song

# Create your views here.

class Tune(View):
    def get(self,request):
        song_info = Song.objects.all()
        d={}
        for i in song_info:
            artist = i.artist_info.name
            if artist in d:
                d[artist]+=1
            else:
                d[artist]=1
        print(d)
        return render (request, 'dashboard.html', {'songs': song_info, 'songs_count':d})
    
    def post(self, request):
        title = request.POST.get('title')
        name = request.POST.get('artist')
        artist_name = Artist(name = name)
        artist_name.save()
        info = Song(title=title, artist_info=artist_name)
        info.save()
        return redirect("dashboard")


