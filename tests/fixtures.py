from typing import Any

import pytest

from tests.factories import UserFactory
from users.models import User


# ----------------------------------------------------------------
@pytest.fixture
def user_auth(client) -> dict[str, Any]:
    """
    A fixture to build user add him to database and authenticate

    Params:
        - client: A Django test client instance

    Returns:
        dict with user from database and auth response data
    """
    user_factory: Any = UserFactory.build()
    client.post(
        '/api/users/reg/',
        {
            'username': user_factory.username,
            'password': user_factory.password,
            'password_repeat': user_factory.password
        }
    )
    user_db: User = User.objects.get(username=user_factory.username)
    response_auth: Any = client.post(
        '/api/users/auth/',
        {
            'username': user_factory.username,
            'password': user_factory.password,
        },
        format='json'
    )
    return {'token': response_auth.data['access'], 'user': user_db}


@pytest.fixture
def user_not_auth(client: Any) -> User:
    """
    A fixture to build user add him to database but not authenticate

    Params:
        - client: A Django test client instance

    Returns:
        dict with user from database and auth response data
    """
    user_factory: Any = UserFactory.build()
    client.post(
        '/api/users/reg/',
        {
            'username': user_factory.username,
            'password': user_factory.password,
            'password_repeat': user_factory.password
        }
    )
    user_db: User = User.objects.get(username=user_factory.username)
    return user_db
