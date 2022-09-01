from django.contrib import admin


from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    fields = ['username', 'first_name', 'last_name']


admin.site.register(CustomUser, CustomUserAdmin)

