import uuid
import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Grabbag(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now=False)
    address = models.TextField(max_length=250)

    class Meta:
        db_table = 'grabbag'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def num_participating(self):
    	return 'Num Participating'
    
