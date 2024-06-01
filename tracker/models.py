from django.db import models


# Create your models here.

class ChanelModel(models.Model):
    username = models.CharField(max_length=100)
    is_synced = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
