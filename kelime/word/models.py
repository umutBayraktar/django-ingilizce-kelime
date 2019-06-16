from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Word(models.Model):

    owner=models.ForeignKey(User,related_name="words",on_delete=models.CASCADE)
    lang_1=models.TextField()
    lang_2=models.TextField()
    image= models.URLField()
    is_active=models.BooleanField()


