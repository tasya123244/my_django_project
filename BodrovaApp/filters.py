import django_filters
from .models import AbcModel

class AbcModelFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains', label='ФИО')
    final_score = django_filters.NumberFilter(label='Итоговая оценка')

    class Meta:
        model = AbcModel
        fields = ['full_name', 'final_score']
