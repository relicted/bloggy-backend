from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from app.posts.models import Post
from app.posts.serializers import UserSerializer, UserCreateSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, \
    RetrieveAPIView
from .serializers import PostsSerializer


class SignUp(GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)


class Posts(ListCreateAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.POST)
        super(Posts, self).create(request, *args, **kwargs)


class Detail(APIView):

    @staticmethod
    def get(request, pk):

        post = get_object_or_404(Post, pk=pk)
        return Response(PostsSerializer(post).data)