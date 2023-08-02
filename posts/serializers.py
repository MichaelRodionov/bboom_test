from typing import Type

from rest_framework import serializers

from posts.models import Post


# ----------------------------------------------------------------
class PostBaseSerializer(serializers.ModelSerializer):
    """
    Base post serializer

    Attrs:
        - user: CharField defines users username
    """
    user = serializers.CharField(source='user.username')

    class Meta:
        model: Type[Post] = Post
        fields: tuple = ('id', 'user', 'title', 'body')


# ----------------------------------------------------------------
class PostCreateSerializer(PostBaseSerializer):
    """
    Post serializer to serialize data

    Attrs:
        - user: HiddenField defines current user
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

