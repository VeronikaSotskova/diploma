from networkx import DiGraph
from rest_framework import serializers


class DiGraphSerializer(serializers.Serializer):
    def to_representation(self, instance: DiGraph):
        nodes = {node: {"name": node} for node in instance.nodes}
        edges = {f"edge{i}": {"source": edge[0], "target": edge[-1]} for i, edge in enumerate(instance.edges)}
        return {
            "nodes": nodes,
            "edges": edges,
            "current_node": instance.current_node if instance.current_node else ""
        }
