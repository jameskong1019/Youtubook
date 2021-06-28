from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from youtube_transcript_api import YouTubeTranscriptApi
from django.shortcuts import render
import json


def page(request):
    pages = []
    transcript_list = YouTubeTranscriptApi.list_transcripts('fE2h3lGlOsk')
    for transcript in transcript_list:
        if transcript.language_code == 'ko':
            for line in transcript.fetch():
                jsonObject = json.loads(json.dumps(line))
                pages.append(json.loads(json.dumps({
                    'startTime': jsonObject["start"],
                    'subscript': jsonObject["text"]
                })))
    context = {'pages': pages}
    return render(request, 'page/page.html', context)
