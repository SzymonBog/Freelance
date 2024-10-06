from django.urls import path, include
from . import views


urlpatterns = [
    path("play/<int:music_id>/", views.play_music),
]