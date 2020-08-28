from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='dog.jpg', upload_to='images')
    bio = models.TextField(default='To improve is to change', max_length=500, blank=True)




