from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    email=models.CharField(max_length=254)


    def __str__(self):
        return f"{self.user.username}" #show how we want it to be displayed
