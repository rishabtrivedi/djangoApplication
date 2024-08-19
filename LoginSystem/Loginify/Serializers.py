from rest_framework import serializers
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'password', 'email']  
