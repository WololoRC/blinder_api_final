from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile, BlockedUsers
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
"""
Views for BlockedUsers model.
"""


@api_view(['GET'])
def get_blocked_users(request, profile_id):
    """
    METHOD: 'POST'

    Get data from User BlockedUsers table.

    Returns:
        A dict od blocked users with keys {<user.name>: <user.id>}
        from BlockedUsers table.
    """
    try:
        blocked_dict = {}

        profile = Profile.objects.get(id=profile_id)
        blocked_users = BlockedUsers.objects.get(owner=profile)

        user_list = blocked_users.blocked_list.all()

        for item in user_list:
            blocked_dict.update({f"{item.user}": f"{item.id}"})

        return Response(
                {'blocked_list': blocked_dict},
                status=status.HTTP_200_OK
        )

    except Profile.DoesNotExist:
        return Response(
            {"error": "Profile does not exist"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['PUT', 'DELETE'])
def put_or_delete_blocked_users(request, profile_id):
    """
    METHODS: 'PUT', 'DELETE'

    A payload called 'id_list' with a list of valid UUID's
    is required.

    Returns: A dict of blocked users on success,
    a error message if 'profile_id' or 'id_list' have
    invalid data.

    PUT:
        Add Users to BlockedUsers main User table.

    DELETE:
        Remove Users of BlockedUsers main User Table.
    """
    try:
        blocked_dict = {}
        profile = Profile.objects.get(id=profile_id)
        data = request.data
        blocked_users = BlockedUsers.objects.get(owner=profile)
        new_blocks = Profile.objects.filter(id__in=data.get('id_list', []))

    except Profile.DoesNotExist:
        return Response({"error": "Profile does not exist"})

    except ValidationError:
        return Response(
            {"error": "some UUID in 'id_list' does no exist or is invalid."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'PUT':
        blocked_users.blocked_list.add(*new_blocks)

    elif request.method == 'DELETE':
        blocked_users.blocked_list.remove(*new_blocks)

    for item in blocked_users.blocked_list.all():
        blocked_dict.update({f"{item.user}": f"{item.id}"})

    return Response(
            blocked_dict,status=status.HTTP_202_ACCEPTED
        )

