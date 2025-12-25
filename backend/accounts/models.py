from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
