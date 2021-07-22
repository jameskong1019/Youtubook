from django.shortcuts import render
from .models import Video
from youtube_transcript_api import YouTubeTranscriptApi
from django.shortcuts import render
import json
import datetime
import urllib.parse
import validators
import sys
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pages.serializers import UserSerializer, GroupSerializer

# fE2h3lGlOsk
# https://youtu.be/TFFtDLZnbSs
# https://www.youtube.com/watch?app=desktop&v=TFFtDLZnbSs&t=325s


def addVideo(youtube_url, video_id):
    existing_url = Video.objects.filter(video_id=video_id)
    if bool(existing_url) == False:
        Video.objects.create(url=youtube_url, video_id=video_id)
        print('Added url:' + youtube_url)


def parse_url(youtube_url):
    if validators.url(youtube_url) == True:
        parsed = urllib.parse.urlparse(youtube_url)
        params = urllib.parse.parse_qs(parsed.query)
        if bool(params):
            video_id = urllib.parse.parse_qs(parsed.query)['v'][0]
        else:
            video_id = youtube_url.rsplit('/', 1)[1]
    else:
        video_id = youtube_url
        youtube_url = 'https://youtu.be/' + video_id
    return video_id


def get_pages(video_id, youtube_url):
    pages = []
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['ko', 'en'])
    for line in transcript.fetch():
        jsonObject = json.loads(json.dumps(line))
        pages.append(json.loads(json.dumps({
            'startTime': jsonObject["start"],
            'formattedTime': str(datetime.timedelta(seconds=jsonObject["start"])),
            'subscript': jsonObject["text"]
        })))
    addVideo(youtube_url, video_id)
    return pages


def page(request):
    try:
        youtube_url = request.POST.get("youtube_url")
        video_id = parse_url(youtube_url)
        context = {
            'pages': get_pages(video_id, youtube_url),
            'video_id': video_id
        }
        return render(request, 'page.html', context)
    except:
        return render(request, 'page.html', {
            'error_message': 'No Script Found. Please Retry Enter a url or id. Thanks:)',
            'stack_trace': sys.exc_info()
        })


def detail(request, video_id):
    existing_url = Video.objects.filter(video_id=video_id)
    context = {
        'pages': get_pages(video_id, existing_url),
        'video_id': video_id
    }
    return render(request, 'page.html', context)


def index(request):
    videos = Video.objects.all()
    context = {'latest_entered_videos': videos}
    return render(request, 'index.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]