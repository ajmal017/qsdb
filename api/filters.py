from django_filters import rest_framework as filters
from api.models import *

class ESFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = ESModel
        fields = ('Date',)
        
class RTYFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = RTYModel
        fields = ('Date',)
        
class SIFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = SIModel
        fields = ('Date',)
        
class QIFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = QIModel
        fields = ('Date',)

class QOFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = QOModel
        fields = ('Date',)
        
class PAFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = PAModel
        fields = ('Date',)
        
class YMFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = YMModel
        fields = ('Date',)
        
class PLFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = PLModel
        fields = ('Date',)
        
class ZSFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = ZSModel
        fields = ('Date',)
        
class GCFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = GCModel
        fields = ('Date',)
        
class M6Filter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = M6Model
        fields = ('Date',)
        
class DYFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = DYModel
        fields = ('Date',)
        
class CLFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = CLModel
        fields = ('Date',)
        
class NGFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = NGModel
        fields = ('Date',)
        
class MESFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = MESModel
        fields = ('Date',)
        
class MNQFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = MNQModel
        fields = ('Date',)
        
class M2KFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = M2KModel
        fields = ('Date',)
        
class MGCFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = MGCModel
        fields = ('Date',)
        
class MYMFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = MYMModel
        fields = ('Date',)
        
class QMFilter(filters.FilterSet):
    Date = filters.DateFromToRangeFilter()
    
    class Meta:
        model = QMModel
        fields = ('Date',)