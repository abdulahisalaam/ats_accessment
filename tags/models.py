from django.db import models


from django_ckeditor_5.fields import CKEditor5Field


from news.models import New

# Create your models here.
class Tag(models.Model):
    title = CKEditor5Field('Text', config_name='extends',null=True,blank=True)
    news = models.ForeignKey(New, on_delete=models.CASCADE)
