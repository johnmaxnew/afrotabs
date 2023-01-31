import django_filters
from .models import *


class HomeFilter(django_filters.FilterSet):
    class Meta:
        model = Home
        # fields = {
        #     '__all__': ['icontains'],
        #     }
        # fields = '__all__'
        # fields = ('title', 'categories')
        # fields = ('categories')
        fields = {'title': ['icontains'],}