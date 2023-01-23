from django.shortcuts import render
from .models import StoryModel, MonstorModel
from django.views.generic.detail import DetailView
from .forms import StoryForm

# Create your views here.

#----------------------------------------------------------------
# Главная страница
def home(reques):
    return render(reques, 'scrimers/home.html') # рендер страницы

#----------------------------------------------------------------
# Страница расказов
def stories(reques):
    stories = StoryModel.objects.all() # получение всех записей из таблицы

     # данные для передачи на страницу
    data = {
        'stories' : stories
    }
    return render(reques, 'scrimers/stories.html', data) # рендер страницы

#----------------------------------------------------------------
# Страница истории
class StoryDetails(DetailView):
    model = StoryModel # модель истории
    template_name = 'scrimers/story.html' # название шаблона
    context_object_name = 'story' # название передаваемого объекта

#----------------------------------------------------------------
# Страница добавления историй
def storyAdd(request):
    form = StoryForm()
    data = {
        'form' : form
    }
    return render(request, 'scrimers/storyAdd.html', data)

#----------------------------------------------------------------
# Страница монстров
def monstors(reques):
    monstors = MonstorModel.objects.all() # получение всех записей из таблицы
    # данные передаваемые на страницу
    data = {
        'monstors' : monstors 
    }
    return render(reques, 'scrimers/monstors.html', data) # рендер страницы

#----------------------------------------------------------------
# Страница монстра
class MonstorDetail(DetailView):
    model = MonstorModel
    template_name = 'scrimers/monstor.html'
    context_object_name = 'monstor'