from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('email is already taken')})
        return attrs

    # create a user

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
