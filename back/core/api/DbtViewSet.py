from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.enums import ModelTypeEnum
from core.serializers import DiGraphSerializer
from core.service import DBTGraphService


class DbtViewSet(viewsets.ViewSet):
    service = DBTGraphService()
    serializer = DiGraphSerializer

    @action(detail=False, methods=['get'])
    def get_dependencies(self, request, *args, **kwargs):
        model_type = request.GET.get('model_type', 'domain')
        model_id = int(request.GET.get('id'))
        model = ModelTypeEnum[model_type].model
        obj = model.objects.get(id=model_id)
        node_name = self.service.find_node_name(model_name=obj.name, model_type=model_type)
        graph = self.service.get_subgraph(node_name)
        if graph:
            graph.current_node = node_name
        return Response(
            {
                "graph": self.serializer(graph).data,
                "entity": ModelTypeEnum[model_type].serializer(obj).data
            }
        )
