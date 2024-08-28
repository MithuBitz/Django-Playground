from django.db import models
from django.utils import timezone

NAME_TYPE_CHOICE = [
        ("MB", "MITHU"),
        ("NB", "NIRANJAN"),
        ("KB", "KHUKHU"),
        ("AB", "ANURAG"),
    ]

# Create your models here.
class NamesList(models.Model):    

    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='avatar/') # need to install Pillow to work
    add_time = models.DateTimeField(default= timezone.now)
    type = models.CharField(max_length=9, choices=NAME_TYPE_CHOICE, default="MB")

    def __str__(self):
        return self.name