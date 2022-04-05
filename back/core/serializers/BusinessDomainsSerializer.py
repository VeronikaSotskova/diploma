from rest_framework import serializers

from core.models import BusinessDomains


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomains
        fields = ["id", "color", "name"]


class BusinessDomainsSerializer(serializers.ModelSerializer):
    has_children = serializers.BooleanField()
    value = serializers.IntegerField()
    type = serializers.CharField()

    def to_representation(self, instance):
        instance.has_children = instance.children.exists() or instance.tables.exists()
        count_tables = instance.tables.count()
        nodes_to_check = list(instance.children.all())
        while len(nodes_to_check) > 0:
            cur_node = nodes_to_check.pop()
            children_node = cur_node.children
            if children_node.exists():
                nodes_to_check.extend(list(children_node.all()))
            count_tables += cur_node.tables.count()

        instance.type = "domain"
        instance.value = count_tables + 1
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = BusinessDomains
        exclude = ["tables", ]
