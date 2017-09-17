import uuid

from django.db import models

from grabbags.models import Grabbag

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

class GiftAssignment(models.Model):
	grabbag_giver = models.ForeignKey('users.User', related_name='grabbag_giver')
	grabbag_receiver = models.ForeignKey('users.User', related_name='grabbag_receiver')
	grabbag = models.ForeignKey(Grabbag)

	class Meta:
		db_table = 'gift_assignment'

	def __str__(self):
		return self.grabbag_giver.first_name + ' is giving a gift to ' + self.grabbag_receiver.first_name