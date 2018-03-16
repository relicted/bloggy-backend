from rest_framework.generics import ListCreateAPIView

from app.posts.models.post import Post
from app.posts.serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
