from rest_framework import serializers
from tweets.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """This serializer allow users to post a new tweet"""
    class Meta:
        model = Post
        fields = ['id','author', 'content', 'created']
        # read_only_fields = ['created']
