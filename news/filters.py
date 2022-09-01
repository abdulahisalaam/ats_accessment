import django_filters 

from .models import New


class NewFilter(django_filters.FilterSet):
    class Meta:
        model = New
        fields = '__all__'
        exclude = ['content']