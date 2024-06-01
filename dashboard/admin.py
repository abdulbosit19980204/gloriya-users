from django.contrib import admin
from .models import entities, AdditionalSourcesModels
import django.db.backends.sqlite3


# Register your models here.
# admin.site.register(entities)


@admin.register(entities)
class EntitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'id')


@admin.register(AdditionalSourcesModels)
class AdditionalSourcesModelsAdmin(admin.ModelAdmin):
    list_display = ('author', 'visitors')
