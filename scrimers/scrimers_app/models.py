from django.db import models

# Create your models here.

class StoryModel(models.Model):
    title = models.CharField('Название', max_length=250)
    date = models.DateField('Дата публикации')
    discription = models.TextField('Описание')
    text = models.TextField('Полный текст')

    def __str__(self):
        return self.title

class MonstorModel(models.Model):
    title = models.CharField('Название', max_length=250)
    disctiption = models.TextField('Описание')

    def __str__(self):
        return self.title
