# Generated by Django 4.1.5 on 2023-01-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrimers_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonstorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('disctiption', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]