from rest_framework import serializers

from core.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    text = serializers.CharField()

    def to_representation(self, instance):
        instance.color = instance.color if instance.color else instance.tag_type.color
        instance.text = f"{instance.tag_type.name}: {instance.name}" \
            if instance.tag_type \
            else f"Other: {instance.name}"
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = Tags
        fields = ('id', 'text', 'color')
