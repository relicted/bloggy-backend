from rest_framework import serializers

from app.accounts.models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'date_joined',
            'email',
            'birthday',
            'country',
            'city',
            'first_name',
            'last_name',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
