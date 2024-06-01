from django.contrib import admin
from .models import ChanelModel


# Register your models here.

@admin.register(ChanelModel)
class ChanelModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_synced', 'created_at', 'updated_at')
