from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    detail = models.TextField(default='')

    def __str__(self):
        return self.name

# One to Many relation between models
class NameReview(models.Model):
    review_name = models.ForeignKey(NamesList, on_delete=models.CASCADE, related_name='reviews') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return f'{self.user.username} review for {self.review_name.name}'
    
# Many to Many relationship
class DevCommunity(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=40)
    name_lists = models.ManyToManyField(NamesList, related_name='devcomm')

    def __str__(self) :
        return self.name
    
# One to One relation
class DevCertificate(models.Model):
    dev_name = models.OneToOneField(NamesList, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self) :
        return f'Certificate for {self.dev_name}'