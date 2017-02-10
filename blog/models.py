from django. db import models
from django. contrib import admin


# Create your models here.
class Blog(models. Model):
    title = models. CharField(max_length=150)
    body = models. TextField()
    timestamp = models. DateTimeField()

    class Admin:
        def __init__(self):
            pass
'''
class File(models.Model):
    filename=models.CharField(max_length=30)
    fileway=models.FileField('C:\Users\Cathy\PycharmProjects\connect')

    def __str__(self):
        return self.filename
'''
admin. site. register(Blog)
