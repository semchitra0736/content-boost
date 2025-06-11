# generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("veo3/", views.veo3, name="veo3"),
    path("youtube-tags/", views.youtube_tags, name="youtube_tags"),
    path("tiktok-tags/", views.tiktok_tags, name="tiktok_tags"),
    path("facebook-reels/", views.facebook_reels, name="facebook_reels"),
]