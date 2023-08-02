from typing import Type

from factory import Faker, Sequence
from factory.django import DjangoModelFactory

from posts.models import Post
from users.models import User


# ----------------------------------------------------------------
class UserFactory(DjangoModelFactory):
    """User factory"""
    class Meta:
        model: Type[User] = User

    username = Faker('user_name')
    password = Faker('password')


# ----------------------------------------------------------------
class PostFactory(DjangoModelFactory):
    """Post factory"""
    class Meta:
        model: Type[Post] = Post

    title = Sequence(lambda x: f'post_{x}')
    body = Sequence(lambda x: f'Body of the post_{x}')
