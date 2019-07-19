from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'stories_index/index.html')

def about(request):
    return render(request, 'stories_index/about.html')

def story(request, story_id):
    return render(request, 'stories_index/story.html')