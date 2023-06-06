"""
Tags django module for Users Profile
"""
import uuid
from django.db import models


class Tags(models.Model):
    """
    Tags table.
    """
    tag_name = models.CharField(max_length=50, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
