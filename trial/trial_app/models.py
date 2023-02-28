from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save #add this
from django.dispatch import receiver #add this
# Create your models here.

class CustomUser(AbstractUser):
    reg_no=models.CharField(max_length=6,unique=True)
    email=models.EmailField(unique=True)
    dept=models.CharField(max_length=4)
    ph_no=models.CharField(max_length=10)


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            profile=Profile.objects.create(user=instance)
            profile.email = instance.email
            profile.save()

    def __str__(self):
        return f"{self.user.username}" #show how we want it to be displayed
    def reg_no(self):
        return f"{self.user.reg_no}"
    def email(self):
        return f"{self.user.email}"
    def dept(self):
        return f"{self.user.dept}"
    def ph_no(self):
        return f"{self.user.ph_no}"
