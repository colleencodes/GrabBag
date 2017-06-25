import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=150, blank=False)
    address = models.TextField(blank=False, null=False)
