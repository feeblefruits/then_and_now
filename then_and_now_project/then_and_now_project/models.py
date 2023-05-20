from django.db import models

class BeforePhoto(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pseudonym = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='before_photos')

class AfterPhoto(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pseudonym = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='after_photos')
