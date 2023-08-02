from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostCreateSerializer, PostBaseSerializer


# ----------------------------------------------------------------
@extend_schema(tags=['Post'])
class PostCreateView(CreateAPIView):
    """
    View to handle POST request to create post entity

    Attrs:
        - permission_classes: defines permissions for this APIView
        - serializer_class: defines serializer class for this APIView
    """
    permission_classes: list = [IsAuthenticated]
    serializer_class = PostCreateSerializer

    @extend_schema(
        description="Create new post instance",
        summary="Create post",
    )
    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().post(request, *args, **kwargs)


# ----------------------------------------------------------------
@extend_schema(tags=['Post'])
class PostListView(ListAPIView):
    """
    View to handle GET request to get list of posts

    Attrs:
        - permission_classes: defines permissions for this APIView
        - serializer_class: defines serializer class for this APIView
    """
    permission_classes: list = [IsAuthenticated]
    serializer_class = PostBaseSerializer

    def get_queryset(self) -> QuerySet[Post]:
        """
        Method to define queryset to get posts by some filters

        Returns:
            - QuerySet
        """
        return Post.objects.filter(user=self.request.user)

    @extend_schema(
        description="Get list of posts",
        summary="Posts list",
    )
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().get(request, *args, **kwargs)


# ----------------------------------------------------------------
@extend_schema(tags=['Post'])
class PostDeleteView(DestroyAPIView):
    """
    View to handle DELETE request to delete post

    Attrs:
        - permission_classes: defines permissions for this APIView
    """
    permission_classes: list = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Post]:
        """
        Method to define queryset to get posts by some filters

        Returns:
            - QuerySet
        """
        return Post.objects.filter(user=self.request.user)

    @extend_schema(
        description="Get list of posts",
        summary="Posts list",
    )
    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().delete(request, *args, **kwargs)
