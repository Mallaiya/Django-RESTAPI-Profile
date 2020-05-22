from rest_framework import serializers
from profiles_api import models

class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'email', 'name', 'dob', 'password']
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            dob=validated_data['dob'],
            password=validated_data['password'],
        )
        return user

