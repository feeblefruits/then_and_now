from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    before_photo = models.ImageField(upload_to='photos/')
    after_photo = models.ImageField(upload_to='photos/')
    pseudonym = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
