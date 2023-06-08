import uuid
from datetime import date
from django.db import models
from django.contrib.auth.models import User
"""
Profile table
"""
class Profile(models.Model):
    """
    Profile model.

    ATRIBUTES:
    ----------
    user:
        User.id related instance.

    description:
        Description of profile.

    owner_tags:
        Tags related to User Profile

    birth_age:
        birth age of User, when you create
        a new instance of Profile insert data
        as follows: (Y/M/D) datetype.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, editable=True)
    owner_tags = models.ManyToManyField('tags.Tags', blank=True)
    birth_date = models.DateField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class BlockedUsers(models.Model):
    """
    Model for blocked users, here comes the bloked users.

    ATRIBUES:
    ---------
    user:
        owner of the record.
    blocked_list:
        list of blocked users.
    """
    owner = models.OneToOneField(Profile, related_name='owner' ,on_delete=models.CASCADE)
    blocked_list = models.ManyToManyField(Profile, blank=True)
