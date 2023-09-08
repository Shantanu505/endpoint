from rest_framework import serializers
from .models import User, UserInput

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = '__all__'
