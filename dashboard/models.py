from django.db import models
from auth_app.models import User


# Create your models here.

class entities(models.Model):
    telegram_id = models.IntegerField(default=0)
    hash = models.IntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name.__str__()


class AdditionalSourcesModels(models.Model):
    visitors = models.IntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.visitors.__str__()
