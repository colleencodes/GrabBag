import uuid
import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=150, blank=False, unique=True)
    address = models.TextField(blank=False, null=False)
    date_of_birth = models.DateTimeField(blank=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def is_adult(self):
        curr_year = year = datetime.datetime.today().year

        comparison_date = \
            datetime.datetime.strptime('1101' + str(curr_year), '%m-%d-%Y')

        if comparison_date - date_of_birth >= 18:
            return True
        else:
            return False

class Family(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, blank=False)

    class Meta:
        db_table = 'family'

    def __str__(self):
        return self.name + ': ' + self.members
