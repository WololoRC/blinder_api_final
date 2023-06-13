from datetime import date
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from tags.serializers import TagsSerializer
"""
Profile and User serializer.
"""

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer.

    Contains username and pk.
    """
    class Meta:
        model = User
        fields = ['username']

class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile Serializer.

    Contains User and Tags serializations, age and description.
    """
    user = UserSerializer()
    owner_tags = TagsSerializer(many=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [ 'user', 'age','id', 'description', 'owner_tags']

    def get_age(self, obj):
        today = date.today()
        return today.year - obj.birth_date.year
