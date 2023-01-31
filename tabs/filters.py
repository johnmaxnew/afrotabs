import django_filters
from .models import *


class TabFilter(django_filters.FilterSet):
    class Meta:
        model = Tab
        # fields = {
        #     '__all__': ['icontains'],
        #     }
        # fields = '__all__'
        # fields = ('title', 'categories')
        # fields = ('categories')
        fields = {'title': ['icontains'],}