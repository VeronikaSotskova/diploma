from rest_framework import serializers

from core.models import Tables


class TablesSerializer(serializers.ModelSerializer):
    has_children = serializers.BooleanField()
    value = serializers.IntegerField()

    def to_representation(self, instance):
        instance.value = 10
        instance.has_children = False
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = Tables
        fields = "__all__"