from profiles.models import Profile
from .models import Chat, Message
from .serializers import ChatSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
"""
message_app views
"""


@api_view(['GET', 'DELETE'])
def get_delete_chat(request, chat_id):
    """
    METHOD: 'GET', 'DELETE'

    GET:
    Get a Chat instance by his 'chat_id'.

    Returns:
    A Chat instance on success, a error message if fails.

    .......................................................

    DELETE:
    Deletes a Chat instance by his 'chat_id'.

    Returns:
    A success nessage on successm, a error message if fails.
    """
    try:
        chat = Chat.objects.get(id=chat_id)

    except (Chat.DoesNotExist, ValidationError):
        return Response(
            {"error": f"'{chat_id}' does not exist or is not valid"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        return Response(ChatSerializer(chat).data)

    if request.method == 'DELETE':
        chat.messages.all().delete()
        chat.delete()

        return Response(
            {"deleted": f"'{chat_id}' was deleted."},
            status=status.HTTP_200_OK
        )

@api_view(['PUT'])
def put_chat(request, chat_id):
    """
    METHOD: 'PUT'.

    Put a new message in a Chat instance.

    A 'chat_id' and a payload with these fiels is required:
    'sender': A profile UUID who sends the message.
    'reciever': A profile UUID who recieve the message.
    'msg_content': A string with the content of message.

    Returns:
    A updated Chat instance on success,
    a ugly error message if fails.

    """
    try:
        data = request.data
        chat = Chat.objects.get(id=chat_id)
        payload_sender = Profile.objects.get(id=data.get('sender'))
        payload_reciever = Profile.objects.get(id=data.get('reciever'))

    except (Chat.DoesNotExist, ValidationError):
        return Response(
            {"error": "'chat_id' does not exist."},
            status=status.HTTP_404_NOT_FOUND
        )

    except ValidationError:
        return Response(
            {'error': "payload has no valid data."},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    except Profile.DoesNotExist:
        return Response(
            {'error': "'sender' or 'reciever' does not exist"},
            status=status.HTTP_404_NOT_FOUND
        )

    message = Message(
        sender=payload_sender,
        reciever=payload_reciever,
        msg_content=data.get('msg_content')
    )

    message.save()

    chat.messages.add(message)

    return Response(ChatSerializer(chat).data)

@api_view(['GET'])
def get_from_user(request, profile_id):
    """
    METHOD: 'GET'.

    Get al Chat instance related to a Profile.

    A valid 'profile_id' on url is required.

    Return:
    All chat instances of User, as 'user_one'
    or 'user_two'.
    """
    try:
        profile = Profile.objects.get(id=profile_id)
        chat_list = []

    except Profile.DoesNotExist:
        return Response(
            {"error": "Profile does not exist"},
            status=status.HTTP_404_NOT_FOUND
    )

    try:
        list_one = Chat.objects.filter(user_one=profile)
    except Chat.DoesNotExist:
        pass

    try:
        list_two = (Chat.objects.filter(user_two=profile))
    except Chat.DoesNotExist:
        pass

    return Response(
            { "as user_one": ChatSerializer(list_one, many=True).data,
            "as user_two": ChatSerializer(list_two, many=True).data}
        )
