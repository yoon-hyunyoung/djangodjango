from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import EPL
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError
class EPLSerializer(ModelSerializer):
    class Meta:
        model = EPL
        fields = '__all__'














