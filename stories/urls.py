from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'), # root path
    path('<int:story_id>', views.story, name='story'),
    path('about', views.about, name='about'),
]

# TODO: In template story.html design dynamic load of data from DB
