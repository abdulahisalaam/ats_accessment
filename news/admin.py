from django.contrib import admin


from .models import New

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    model = New
    fields = ['title','content','author','schedule_time']


admin.site.register(New, NewsAdmin)