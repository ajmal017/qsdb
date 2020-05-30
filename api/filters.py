from django_filters import rest_framework as filters
from api.models import PAModel

class PAFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = PAModel
        fields = ('Date',)