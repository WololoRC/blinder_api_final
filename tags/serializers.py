from rest_framework import serializers
from .models import Tags


"""
Serializer for Tags module
"""
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag_name', 'id']
