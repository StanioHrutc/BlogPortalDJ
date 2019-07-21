from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . models import Story
# for fetching data from DB


def index(request):
    stories = Story.objects.all()

    # TODO: to make it work type: pip install pylint-django
    context = {
        # some data tu put in render function
        'stories': stories,
    }
    return render(request, 'stories_index/index.html', context)

def about(request):
    return render(request, 'stories_index/about.html')

def story(request, story_id):
    return render(request, 'stories_index/story.html')