from rest_framework.generics import ListCreateAPIView

from app.posts.models.post import Post
from app.posts.serializers import PostSerializer

import time


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get(self, request, *args, **kwargs):
        time.sleep(5)
        return super(PostList, self).get(request, *args, **kwargs)
