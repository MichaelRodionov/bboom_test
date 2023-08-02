from drf_spectacular.utils import extend_schema
from requests import Request, Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserRegSerializer, UserListSerializer


# ----------------------------------------------------------------
# user views
@extend_schema(tags=['User'])
class UserRegView(CreateAPIView):
    """
    View to handle registration

    Attrs:
        - serializer_class: defines serializer class for this APIView
    """
    serializer_class = UserRegSerializer

    @extend_schema(
        description="Create new user instance",
        summary="Registrate user",
    )
    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().post(request, *args, **kwargs)


# ----------------------------------------------------------------
@extend_schema(tags=['User'])
class UserAuthView(TokenObtainPairView):
    """Custom TokenObtainPairView to handle user authentication and add description to openapi documentation"""
    @extend_schema(
        description="Get access and refresh JWT token",
        summary="Authenticate user",
    )
    def post(self, request: Request, *args: tuple, **kwargs: dict):
        return super().post(request, *args, **kwargs)


# ----------------------------------------------------------------
@extend_schema(tags=['User'])
class UserListView(ListAPIView):
    """
    View to handle get request to get list of all users

    Attrs:
        - queryset: defines queryset for this APIView
        - serializer_class: defines serializer class for this APIView
        - permission_classes: defines permissions for this APIView
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes: list = [IsAuthenticated]

    @extend_schema(
        description="Get list of all users",
        summary="Get users",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
