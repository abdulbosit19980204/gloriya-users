from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ChanelModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model: ChanelModel
        fields = '__all__'
