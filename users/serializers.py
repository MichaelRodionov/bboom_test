from typing import Any, Type

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User


# ----------------------------------------------------------------
# user serializer
class UserRegSerializer(serializers.ModelSerializer):
    """
    User registration serializer

    Attrs:
        - password: current user's password
        - password_repeat: repeat of current password
    """
    password = serializers.CharField(required=True, write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def validate(self, attrs) -> Any:
        """
        Redefined method to validate incoming data

        Params:
            - validated_data: dictionary with validated data of User entity

        Returns:
            - attrs: dictionary with data

        Raises:
            - ValidationError (in case of password repeat is wrong)
        """
        password_repeat = attrs.pop('password_repeat')

        if attrs.get('password') != password_repeat:
            raise serializers.ValidationError('Password mismatch')

        validate_password(attrs.get('password'))
        return attrs

    def create(self, validated_data) -> Any:
        """
        Redefined create method to create user instance, set password hash, save password hash in db

        Params:
            - validated_data: dictionary with validated data of User instance

        Returns:
            - user: user object
        """
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    class Meta:
        model: Type[User] = User
        fields: tuple = ('id', 'username', 'email', 'password', 'password_repeat')


# ----------------------------------------------------------------
class UserListSerializer(serializers.ModelSerializer):
    """Serializer for list of users"""
    class Meta:
        model: Type[User] = User
        fields: tuple = ('id', 'username', 'email')
