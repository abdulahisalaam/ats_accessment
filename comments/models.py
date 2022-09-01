from django.db import models


from django_ckeditor_5.fields import CKEditor5Field


from accounts.models import CustomUser as User
from news.models import New


# Create your models here.
class Comment(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='news')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field('Text', config_name='extends',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
