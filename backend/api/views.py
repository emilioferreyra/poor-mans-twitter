from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
from tweets.models import Post


class PostViewSet(viewsets.ModelViewSet):
    """This view allow users list all tweets"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
