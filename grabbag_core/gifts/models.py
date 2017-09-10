import uuid

from django.db import models

class Gift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=500)
    link = models.URLField(max_length=500)
    photo = models.ImageField(upload_to='gift_pics')

    class Meta:
    	db_table = 'gift'

    def __str__(self):
    	return 'Gift: ' + self.title
