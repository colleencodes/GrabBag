import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    address = models.TextField(blank=False, null=False)

    def __str__(self):
    	return self.first_name + ' ' + self.last_name
