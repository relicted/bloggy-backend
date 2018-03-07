from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from app.accounts.models import User
from app.accounts.serializers import UserListSerializer, UserCreateSerializer


class UsersList(APIView):

    @staticmethod
    def get(request):

        users = User.objects.all()
        return Response(UserListSerializer(users, many=True).data)


    @staticmethod
    def post(request):

        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(UserCreateSerializer(user).data)

        return Response(serializer.errors)