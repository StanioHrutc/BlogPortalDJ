from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from . models import Story
# for fetching data from DB

from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Story)
def my_handler(sender, **kwargs):
    print('Object is saved')
# changed -> add sending emails


stories = Story.objects.order_by('-publication_date').filter(is_published=True)
# TODO: to make it work typo: pip install pylint-django
context = {
    # some data tu put in render function
    'stories': stories,
}


def index(request):
    paginator     = Paginator(stories, 3)
    page          = request.GET.get('page')
    paged_stories = paginator.get_page(page)
    context       = {
        'stories': paged_stories,
    }

    return render(request, 'stories_index/index.html', context)


def story(request, story_id):
    story         = get_object_or_404(Story, pk=story_id)
    previous_page = request.META['HTTP_REFERER']

    return render(request, 'stories_index/story.html', {'story': story, 'back': previous_page})


def about(request):
    return render(request, 'stories_index/about.html')

