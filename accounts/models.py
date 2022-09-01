import uuid

from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True,help_text='enter nick name here ...')
    first_name = models.CharField(max_length=200, help_text='enter your firstname ...')
    last_name = models.CharField(max_length=200, help_text='enter your lastname ...')
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse("user-details", kwargs={'pk':self.id})
    