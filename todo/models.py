from django.db import models


class Item(models.Model):
    """
    Model for creating list items.
    """
    objects = models.Manager()

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)

    category = models.TextField(max_length=12)
    description = models.TextField(max_length=200)
    term = models.TextField(max_length=20)

    finish_by = models.DateTimeField()

    is_completed = models.BooleanField()
