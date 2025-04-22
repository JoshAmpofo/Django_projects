from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Enzyme

class EnzymeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('curator', 'name', 'ec_number', 'temperature', 'description', 'created_at',)
        model = Enzyme
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)