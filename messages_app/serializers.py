from rest_framework import serializers
from .models import Message, Chat
from profiles.serializers import ProfileSerializer
from profiles.models import Profile
"""Serializers for Chat and Message models."""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    reciever = UserSerializer()

    class Meta:
        model = Message
        fields = ['reciever', 'sender', 'msg_content', 'created_at']


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    user_one = ProfileSerializer()
    user_two = ProfileSerializer()

    class Meta:
        model = Chat
        fields = ['user_one', 'user_two', 'messages', 'id']


