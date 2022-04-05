from rest_framework import serializers

from core.models import Tables


class TablesDropdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ["id", "name"]
