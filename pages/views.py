from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from youtube_transcript_api import YouTubeTranscriptApi
from django.shortcuts import render
import json
import datetime
import urllib.parse
import validators
import sys

# fE2h3lGlOsk
# https://youtu.be/TFFtDLZnbSs
# https://www.youtube.com/watch?app=desktop&v=TFFtDLZnbSs&t=325s

def addVideo(youtube_url):
    existing_url=Video.objects.filter(url=youtube_url)
    if bool(existing_url) == False:
        Video.objects.create(url=youtube_url)
        print('added url:' + youtube_url)


def page(request):
    youtube_url = request.POST.get("youtube_url")
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
    pages = []
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['ko', 'en'])
        for line in transcript.fetch():
            jsonObject = json.loads(json.dumps(line))
            pages.append(json.loads(json.dumps({
                'startTime': jsonObject["start"],
                'formattedTime': str(datetime.timedelta(seconds=jsonObject["start"])),
                'subscript': jsonObject["text"]
            })))
        context = {
            'pages': pages,
            'video_id': video_id
        }
        addVideo(youtube_url)
        return render(request, 'page.html', context)
    except:
        return render(request, 'page.html', {
            'error_message': 'No Script Found. Please Retry Enter a url or id. Thanks:)',
            'stack_trace': sys.exc_info()
        })

def index(request):
    videos = Video.objects.all()
    context = {'latest_entered_videos': videos}
    return render(request, 'index.html', context)