from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from youtube_transcript_api import YouTubeTranscriptApi
from django.shortcuts import render
import json
import datetime
import urllib.parse
import validators
import sys

# fE2h3lGlOsk

def page(request):
    youtube_url = request.POST.get("youtube_url")
    if validators.url(youtube_url) == True:
        parsed = urllib.parse.urlparse(youtube_url)
        video_id = urllib.parse.parse_qs(parsed.query)['v'][0]
    else:
        video_id = youtube_url
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
        return render(request, 'page.html', context)
    except:
        return render(request, 'page.html', {
            'error_message': 'No Script Found. Please Retry Enter a url or id. Thanks:)',
            'stack_trace': sys.exc_info()[0]
        })

def index(request):
    return render(request, 'index.html')
