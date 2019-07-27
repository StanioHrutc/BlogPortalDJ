from django.shortcuts import render

from .models import Work
# Create your views here.


def works(request):

    works = Work.objects.all()

    context = {
        'works': works
    }

    return render(request=request,
                  template_name='works/works.html',
                  context=context)
