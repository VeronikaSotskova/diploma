from rest_framework import serializers

from core.models import Tables
from core.serializers.TagsWithCountSerializer import TagsWithCountSerializer


class TablesSerializer(serializers.ModelSerializer):
    has_children = serializers.BooleanField()
    value = serializers.IntegerField()
    type = serializers.CharField()
    tags = TagsWithCountSerializer(read_only=True, many=True)

    def to_representation(self, instance):
        instance.value = 1
        instance.has_children = False
        instance.type = "table"
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = Tables
        fields = "__all__"
