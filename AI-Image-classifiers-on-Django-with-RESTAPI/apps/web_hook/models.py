from django.db import models

# Create your models here.
class photo(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'img/')