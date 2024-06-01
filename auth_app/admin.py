from django.contrib import admin

from .models import MyUser, UserType

admin.site.register(MyUser)
admin.site.register(UserType)
