from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=20, null= False, default = 'Anonymous')
    content = models.TextField(null=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Diaries'



class ToDo(models.Model):
    task = models.TextField(null = False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name_plural = 'ToDo-list'