from django.db.models import Q
from django_filters import rest_framework as filters


class TagFilter(filters.FilterSet):
    name = filters.CharFilter(
        label="Название тега",
        method="filter_name",
        help_text="Название тега"
    )

    def filter_name(self, queryset, name, value):
        return queryset.filter(Q(name__istartswith=value) | Q(tag_type__name__istartswith=value))
