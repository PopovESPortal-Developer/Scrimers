from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import StoryModel


class StoryForm(ModelForm):
    class Meta:
        model = StoryModel
        fields = ['title', 'date', 'discription', 'text']

        widgets = {
            'title' : TextInput(attrs={
                'class' : 'title-story',
                'placeholder' : 'Название истории'
            }),
            'date' : DateInput(attrs={
                'class' : 'date-story',
                'placeholder' : 'Дата публикации'
            }),
            'discription' : Textarea(attrs={
                'class' : 'discription-story',
                'placeholder' : 'Краткое описание'
            }),
            'text' : DateInput(attrs={
                'class' : 'text-story',
                'placeholder' : 'Полный текст'
            }),
        }