from django.db import models

# Create your models here.
from news.models import New

# Create your models here.
class Category(models.Model):
    cartegory = models.CharField(max_length=200, null=True, default="Sport", blank=True)
    news = models.ForeignKey(New, on_delete=models.CASCADE, related_name='newss', null=True, blank=True)
    name = models.CharField('CATEGORY', max_length=50)

    def __str__(self):
        return f'{self.name}'