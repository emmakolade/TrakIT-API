from rest_framework import serializers, exceptions
from .models import User
from django.contrib.auth import authenticate


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


# email Verification
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=558)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=50, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('tokens', 'email', 'password', 'username')

        read_only_fields = ['tokens', 'username']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('email', '')

        user = authenticate(email=email, password=password)
        if not user:
            raise exceptions.AuthenticationFailed(
                'invalid credentials, try again')

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                'account disabled, contact admin')
        if not user.is_verified:
            raise exceptions.AuthenticationFailed('email is not verified')
        return {'email': user.email, 'username': user.username, 'tokens': user.tokens()}
