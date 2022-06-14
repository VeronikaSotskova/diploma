from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.enums import ModelTypeEnum
from core.models import BusinessDomains, Tables
from core.serializers import BusinessDomainsSerializer, TablesSerializer, PaginationSerializer
from core.serializers.BusinessDomainsSerializer import ParentSerializer


class BusinessDomainsViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def domains(self, request, *args, **kwargs):
        params = request.GET
        if "id" in params:
            domain = BusinessDomains.objects.filter(id=params["id"]).first()
            resp = ParentSerializer(domain, context={"request": request}).data
            tables = TablesSerializer(domain.tables.all(), many=True, context={"request": request}).data
            bds = BusinessDomainsSerializer(domain.children.all(), many=True,
                                            context={"request": request}).data
            resp["children"] = tables + bds
            return Response(resp)
        qs = BusinessDomains.objects.filter(parent__isnull=True)
        tables = Tables.objects.filter(tables_in_domains__business_domain__isnull=True)
        domains_list = BusinessDomainsSerializer(qs, many=True, context={"request": request}).data
        tables_list = TablesSerializer(tables, many=True, context={"request": request}).data
        return Response(
            {"name": "main", "children": domains_list + tables_list,
             "color": "#ffffff", "stroke": "#000000"}
        )

    @action(detail=False, methods=['get'])
    def hint_objects(self, request, *args, **kwargs):
        params = request.GET
        if "q" in params and params.get("q", None) != "":
            tables = Tables.objects.filter(name__istartswith=params["q"]).values_list("name", flat=True)
            domains = BusinessDomains.objects.filter(name__istartswith=params["q"]).values_list("name", flat=True)
            return Response(list(tables) + list(domains))
        else:
            return Response([])

    @action(detail=False, methods=['patch'])
    def change_color(self, request, *args, **kwargs):
        t = request.data.get('type')
        id_t = request.data.get('id')
        color = request.data.get('color')
        model = ModelTypeEnum[t].model
        model.objects.filter(id=int(id_t)).update(color=color)
        return Response("OK")

    @action(detail=False, methods=['get'])
    def search(self, request, *args, **kwargs):
        params = request.GET
        query = Q()

        paginator_domain = PaginationSerializer()
        paginator_table = PaginationSerializer()

        paginator_domain.page_query_param = 'page_domain'
        paginator_table.page_query_param = 'page_table'

        if "name" in params and params["name"] not in [None, ""]:
            query.add(Q(name__istartswith=params["name"]), Q.AND)
        if "tags" in params and params["tags"] not in [None, ""]:
            tags_list_id = list(map(int, params["tags"].split(",")))
            query.add(Q(tags__in=tags_list_id), Q.AND)
        search_domains = BusinessDomains.objects.filter(query).distinct().order_by("name")
        search_tables = Tables.objects.filter(query).distinct().order_by("name")

        result_page_domains = paginator_domain.paginate_queryset(search_domains, request)
        result_page_tables = paginator_table.paginate_queryset(search_tables, request)

        domains_response = BusinessDomainsSerializer(result_page_domains, many=True, context={"request": request}).data
        tables_response = TablesSerializer(result_page_tables, many=True, context={"request": request}).data

        return Response({
            "domain": paginator_domain.get_paginated_response(domains_response),
            "table": paginator_table.get_paginated_response(tables_response)
        })
