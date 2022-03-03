from django.shortcuts import render
from  youtube_transcript_api import YouTubeTranscriptApi as yta
import re

# Create your views here.

def convert(request):
    if request.method == 'POST':  
        link = request.POST['link']
        index = link.index('=')
        vid_id = link[index+1:]
        data = yta.get_transcript(vid_id)
        transcript = ''
        for value in data:
            for key,val in value.items():
                if key == 'text':
                    transcript += (val+" ")
        #print(transcript)
        return render(request,'result.html',{'transcript':transcript})
    else:
        return render(request,'index.html')
