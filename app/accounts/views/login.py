from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from app.accounts.models.user import User
from app.accounts.serializers.user import UserLoginSerializer


class Login(APIView):

    @staticmethod
    def post(request):

        user = get_object_or_404(User, email__iexact=request.data.get('email'))

        user = authenticate(username=user.email,
                            password=request.data.get('password'))
        if user:
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
