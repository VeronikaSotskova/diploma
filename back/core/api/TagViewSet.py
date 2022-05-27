from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.enums import ModelTypeEnum
from core.filters import TagFilter
from core.models import Tags
from core.serializers import TagsWithCountSerializer


class FilterBackend(DjangoFilterBackend):
    filterset_class = TagFilter

    def get_filterset_class(self, view, queryset=None):
        return self.filterset_class


class TagViewSet(viewsets.ViewSet):
    filter_backend = FilterBackend()
    queryset = Tags.objects.all()

    @action(detail=False, methods=['get'])
    def tags(self, request, *args, **kwargs):
        qs = self.filter_backend.filter_queryset(request, self.queryset, self).order_by("name")
        min_tags_count = request.GET.get('min')
        if min_tags_count:
            qs = qs[:int(min_tags_count)]
        return Response(TagsWithCountSerializer(qs, many=True).data)

    @action(detail=False, methods=['patch'])
    def add_tags(self, request, *args, **kwargs):
        t = request.data.get('type')
        id_t = request.data.get('id')
        tags_param = request.data.get('tags_id')

        model = ModelTypeEnum[t].model
        obj = model.objects.filter(id=int(id_t)).first()

        if tags_param in [None, ""]:
            obj.tags.clear()
        else:
            tags_id = list(map(int, request.data.get('tags_id').split(",")))
            tags_added = Tags.objects.filter(id__in=tags_id)
            obj.tags.set(tags_added)
        return Response(TagsWithCountSerializer(obj.tags.all(), many=True).data)

    @action(detail=False, methods=['get'])
    def tags_for_obj(self, request, *args, **kwargs):
        qs = self.filter_backend\
            .filter_queryset(request, self.queryset, self)\
            .order_by("name")
        return Response(TagsWithCountSerializer(qs, many=True).data)



