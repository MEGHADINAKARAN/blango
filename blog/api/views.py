from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadOnly
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer