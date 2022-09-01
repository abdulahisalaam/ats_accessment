from datetime import datetime
import uuid

from django_ckeditor_5.fields import CKEditor5Field

from django.urls import reverse
from django.db import models


from accounts.models import CustomUser as User



# Create your models here.
class New(models.Model):
    STATUS = (("Draft","DRAFT"), ("Public","PUBLIC"))
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100, help_text='enter nick name here ...')
    status = models.CharField(
                max_length=10, choices=STATUS, default="STATUS", db_index=True
            )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Authors", null=True, blank=True)
    content = CKEditor5Field('Contents', config_name='extends',null=True,blank=True, help_text="News Here ")
    published = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='favourite', blank=True)
    schedule_time = models.DateTimeField(default=datetime.now, null=True,blank=True, editable=True)
    

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('news-details', kwargs={'pk': self.id})

    @property
    def is_due(self):
        return bool(self.schedule_time >= datetime.now())

    class Meta:
        ordering = ['-created_at']

    
    
    

