from django.db import models


# Create your models here.
class Note(models.Model):
    note = models.CharField(max_length=180)
