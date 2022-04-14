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
        config_root = []
        res = {}
        if name is not None and str(name).strip() != "":
            tables = Tables.objects.filter(name__istartswith=name)
            config_root = [f"table_{t_id}" for t_id in list(tables.values_list("id", flat=True))]
            for table in tables:
                domain_ids = table.tables_in_domains.values_list("business_domain", flat=True)
                business_domains = BusinessDomains.objects.filter(id__in=domain_ids)
                res[f"table_{table.id}"] = {
                    "text": table.name,
                    "children": [f"domain_{d_id}" for d_id in list(business_domains.values_list("id", flat=True))]
                }
                for domain in business_domains:
                    res[f"domain_{domain.id}"] = {
                        "text": domain.name,
                    }
                    if domain.parent:
                        res[f"domain_{domain.id}"]["children"] = [f"domain_{domain.parent.id}",]
                    current_domain = domain
                    while current_domain.parent:
                        current_domain = current_domain.parent
                        res[f"domain_{current_domain.id}"] = {
                            "text": current_domain.name,
                        }
                        if current_domain.parent:
                            res[f"domain_{current_domain.id}"]["children"] = [f"domain_{current_domain.parent.id}",]

        return Response({"nodes": res, "config": {"roots": config_root}})

    @action(detail=False, methods=['get'])
    def change_color(self, request, *args, **kwargs):
        t = request.GET.get('type')
        id_t = request.GET.get('id')
        color = request.GET.get('color')
        model = BusinessDomains if t == 'domain' else Tables
        model.objects.filter(id=int(id_t)).update(color=color)
        return Response("OK")


