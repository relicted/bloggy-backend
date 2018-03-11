from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.accounts.serializers.user import (
    UserCreateSerializer,
    UserLoginSerializer
)

import time


class Register(APIView):
    """
      post:
      Create a new user \n
      Required data: email, password, first_name, last_name
    """

    @staticmethod
    def post(request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            time.sleep(5)

            return Response(UserLoginSerializer(user).data,
                            status=status.HTTP_201_CREATED)
        time.sleep(5)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
