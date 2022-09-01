from django.contrib.auth.forms import UserCreationForm


from .models import CustomUser as User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
