from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

class webtoons(models.Model):
    title=models.CharField(max_length=50,null=True)
    thumbnile=models.ImageField(upload_to="thumbline/")
    creator=models.CharField(max_length=50,null=True)
    genre=models.CharField(max_length=50,null=True)
    brief_description=models.TextField(null=True)
    description=models.TextField(null=True)
    
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webtoon = models.ForeignKey(webtoons, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'webtoon')

class Comment(models.Model):
    webtoon = models.ForeignKey(webtoons, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField() 


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
