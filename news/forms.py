from django import forms

from .widgets import DatePickerInput


from .models import New

class NewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title','schedule_time','content')
        widget = {
            'schedule_time': DatePickerInput(),
        }