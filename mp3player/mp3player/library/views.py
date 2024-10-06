from django.shortcuts import render
from django.http import FileResponse
import requests

# Create your views here.
def play_music(request, music_id):
    music_response = requests.get(music_id, stream=True)
    content_type = music_response.headers.get('content-type', 'audio/mpeg')
    return FileResponse(request, music_response.raw, content_type=content_type)
