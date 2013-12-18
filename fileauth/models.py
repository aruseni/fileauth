from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class AuthenticationKey(models.Model):
    key = models.CharField(max_length=40, db_index=True)
    user = models.ForeignKey(User)
    created = models.DateTimeField(
        default=timezone.now
    )
    active = models.BooleanField(default=True)
