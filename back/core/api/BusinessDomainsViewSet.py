from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import BusinessDomains, Tables
from core.serializers import BusinessDomainsSerializer, TablesSerializer
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
