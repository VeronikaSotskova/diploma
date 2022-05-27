from rest_framework import serializers

from core.models import BusinessDomains
from core.serializers.TagsWithCountSerializer import TagsWithCountSerializer


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomains
        fields = ["id", "color", "name"]


class BusinessDomainsSerializer(serializers.ModelSerializer):
    has_children = serializers.BooleanField()
    value = serializers.IntegerField()
    type = serializers.CharField()
    tags = TagsWithCountSerializer(read_only=True, many=True)

    def to_representation(self, instance):
        instance.has_children = instance.children.exists() or instance.tables.exists()
        instance.type = "domain"
        instance.value = instance.tables.count() + instance.children.count() + 1
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = BusinessDomains
        exclude = ["tables", ]
