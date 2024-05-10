from django.db import models

class ImageEmail(models.Model):
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')
