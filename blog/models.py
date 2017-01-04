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

admin. site. register(Blog)
