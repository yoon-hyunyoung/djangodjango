from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import EPL, EPLGroup, Bigmatch, BigmatchGroup
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'


class EPLSerializer(ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')
    class Meta:
        model = EPL
        fields = '__all__'
        labels  = {     
        'group':'연고지'
        }
class EPLGroupSerializer(ModelSerializer):
    class Meta:
        model = EPLGroup
        fields = '__all__'
        

class BigmatchSerializer(ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')
    class Meta:
        model = Bigmatch
        fields = '__all__'
        














