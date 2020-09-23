from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import EPL, EPLGroup
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError
class EPLSerializer(ModelSerializer):
    class Meta:
        model = EPL
        fields = '__all__'

class EPLGroupSerializer(ModelSerializer):
    class Meta:
        model = EPLGroup
        fields = '__all__'

# class BigmatchSerializer(ModelSerializer):
#     class Meta:
#         model = Bigmatch
#         fields = '__all__'
        














