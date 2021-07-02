from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from youtube_transcript_api import YouTubeTranscriptApi
from django.shortcuts import render
import json
import datetime
# fE2h3lGlOsk
video_id = 'fE2h3lGlOsk'
def page(request):
    pages = []
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    for transcript in transcript_list:
        if transcript.language_code == 'ko':
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
