from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import Signal, User

class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signal
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'