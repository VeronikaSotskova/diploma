from rest_framework import serializers

from core.serializers.TagsSerializer import TagsSerializer


class TagsWithCountSerializer(TagsSerializer):
    weight = serializers.IntegerField()

    def to_representation(self, instance):
        instance.weight = instance.tables.all().count() + instance.domains.all().count()
        representation = super().to_representation(instance)
        return representation

    class Meta(TagsSerializer.Meta):
        fields = TagsSerializer.Meta.fields + ('weight',)
