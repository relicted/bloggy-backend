from rest_framework import serializers

from app.posts.models import Post
from app.accounts.serializers.user import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'id', 'title', 'body', 'image')
