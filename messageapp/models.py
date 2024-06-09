from django.db import models

# Create your models here.

import uuid
class Message(models.Model):
    account_id = models.CharField(max_length=255)
    message_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender_number = models.CharField(max_length=15)
    receiver_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.sender_number} -> {self.receiver_number}'

