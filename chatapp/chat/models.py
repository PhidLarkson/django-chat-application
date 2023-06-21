from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, auto_created=True, default=uuid.uuid4, max_length=16)
    name = models.CharField(blank=False, max_length=64)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}|{self.id}"