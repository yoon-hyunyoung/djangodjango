from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Students, Scores
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    
    #reg_user = UserSerializer(read_only=True) #등록때 사용하지않겠다.
    reg_user_username = serializers.ReadOnlyField(source='reg_user.username')
    reg_user_email = serializers.ReadOnlyField(source='reg_user.email')
    test = serializers.SerializerMethodField()
    def get_test(self, obj):
        return obj.address + " (" + obj.name + ")"
    class Meta:
        model = Students
        fields = ['id','name', 'address', 'email', 'memo', 'reg_user', 'reg_user_username', 'reg_user_email', 'reg_user', 'test']




class ScoreSerializer(ModelSerializer):
    reg_user_username = serializers.ReadOnlyField(source='reg_user.username')
    reg_user_email = serializers.ReadOnlyField(source='reg_user.email')
    reg_user_phone_number = serializers.ReadOnlyField(source='reg_user.phone_number')
    
    class Meta:
        model = Scores
        fields = ['id','name', 'math', 'science', 'english', 'reg_user', 'reg_user_username', 'reg_user_email', 'reg_user_phone_number']
    
    def validate_math(self, math):
        if not(0 <= math <= 100):
            raise ValidationError("0~100 사이만 입력해주세요!")
        return math
    def validate_science(self, science):
        if not(0 <= science <= 100):
            raise ValidationError("0~100 사이만 입력해주세요!")
        return science
    def validate_english(self, english):
        if not(0 <= english <= 100):
            raise ValidationError("0~100 사이만 입력해주세요!")
        return english

    # def validate(self, data):
    #     if len(data['name']) < 3:
    #         raise ValidationError("3글자 이상 입력하시오!!")
    #     return data
            
        

class StudentBasicSerializer(Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.CharField()
    def create(self, validated_data):
        Students.objects.create()
        return Students.objects.create(**validated_data)
        #return Students.objects.create(name=validated_data['name'], address=validated_data['address'])
    #student, data=request.data
    #inctance 원래데이터 (student)
    #validated_data 사람이 보내준 데이터 (data=request.data)
    #(원래데이터 <- 사람이 보내준 데이터) -> SAVE 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.name)
        instance.email = validated_data.get('email', instance.name)
        instance.save()
        return instance

class ScoreBasicSerializer(Serializer):
    name = serializers.CharField()
    math = serializers.CharField()
    science = serializers.CharField()
    english = serializers.CharField()
    def create(self, validated_data):
        Scores.objects.create()
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.math = validated_data.get('math', instance.math)
        instance.science = validated_data.get('science', instance.science)
        instance.english = validated_data.get('english', instance.english)
        instance.save()
        return instance
    