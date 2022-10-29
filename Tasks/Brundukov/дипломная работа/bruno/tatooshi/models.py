from datetime import date
from email.policy import default
from tabnanny import verbose
from turtle import mode, title
from django.db import models

# Create your models here.
class Artiles(models.Model):
    title= models.CharField(("название"), max_length=50,default='Введите текст..')
    anons= models.CharField(("АНОНС"), max_length=250,default='Введите текст..')
    full_text=models.TextField('статья')
    date=models.DateTimeField('ВРЕМЯ АНОНСА')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="ОТЗЫВ"
        verbose_name_plural="ОТЗЫВЫ"