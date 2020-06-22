from django.db import models

# Create your models here.
class Result(models.Model):
    title=models.CharField(max_length=100)
    summary=models.TextField()
    file_dest=models.CharField(max_length=200)