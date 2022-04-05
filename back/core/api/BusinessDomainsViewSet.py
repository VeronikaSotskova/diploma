from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from core.models import BusinessDomains, Tables
from core.serializers import BusinessDomainsSerializer, TablesSerializer, TablesDropdownSerializer
from core.serializers.BusinessDomainsSerializer import ParentSerializer
from core.utils import get_path_domain


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
    def tables(self, request, *args, **kwargs):
        params = request.GET
        if "q" in params:
            tables = Tables.objects.filter(name__istartswith=params["q"]).values_list("name", flat=True)
            return Response(list(tables))
        else:
            return Response([])

    @action(detail=False, methods=['get'])
    def table_hierarchy(self, request, *args, **kwargs):
        name = request.GET.get("name", None)
        result = []
        if name is not None and str(name).strip() != "":
            tables = Tables.objects.filter(name__icontains=name)
            for table in tables:
                path = {"id": table.id, "name": table.name, "children": [], "type": "table"}
                domain_ids = table.tables_in_domains.values_list("business_domain", flat=True)
                business_domains = BusinessDomains.objects.filter(id__in=domain_ids)
                for domain in business_domains:
                    domain_path = get_path_domain(domain)
                    path["children"].append({
                        "id": table.id,
                        "name": table.name,
                        "children": domain_path,
                        "type": "table"
                    })
                result.append(path)

        return Response(result)

