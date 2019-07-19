from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # root path
    path('story/<int:story_id>', views.story, name='story'),
    path('about', views.about, name='about'),
]