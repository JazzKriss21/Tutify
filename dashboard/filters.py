import django_filters
from django_filters import CharFilter
from profile_info.models import TutorProfile

class TutorFilter(django_filters.FilterSet):
    subjects=CharFilter(field_name='subjects',lookup_expr='icontains')
    class Meta:
        model=TutorProfile
        fields=['subjects','location']

