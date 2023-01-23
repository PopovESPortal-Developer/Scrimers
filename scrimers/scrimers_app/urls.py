from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stories', views.stories, name='stories'),
    path('stories/<int:pk>', views.StoryDetails.as_view(), name='story'),
    path('monstors', views.monstors, name='monstors'),
    path('monstors/<int:pk>', views.MonstorDetail.as_view(), name='monstor'),
    path('story/add', views.storyAdd, name='storyAdd')
]