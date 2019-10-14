from django.db import models

# Create your models here.

class Qu(models.Model):
    title = models.CharField(max_length=150)
    choice1 = models.CharField(max_length=150)
    choice2 = models.CharField(max_length=150)
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    image_url1 = models.CharField(max_length=200)
    image_url2 = models.CharField(max_length=200)

class An(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(Qu, on_delete=models.CASCADE)