from rest_framework import serializers

from core.models import BusinessDomains


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomains
        fields = ["id", "color", "name"]


class BusinessDomainsSerializer(serializers.ModelSerializer):
    has_children = serializers.BooleanField()
    value = serializers.IntegerField()

    def to_representation(self, instance):
        instance.has_children = instance.children.exists() or instance.tables.exists()
        instance.value = 10
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = BusinessDomains
        exclude = ["tables", ]
