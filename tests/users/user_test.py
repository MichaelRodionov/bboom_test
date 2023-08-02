from typing import Any

import pytest
from rest_framework.exceptions import ErrorDetail

from tests.factories import UserFactory
from users.models import User


# ----------------------------------------------------------------
class TestUser:
    @pytest.mark.django_db
    def test_registrate_user(self, client: Any) -> None:
        """
        User registration success test

        Params:
            - client: A Django test client instance.

        Checks:
            - Response status code is 201
            - Response data is not None
            - user from database exists
            - users username is equal to username of user from user factory

        Returns:
            None

        Raises:
            AssertionError
        """
        user_factory, reg_response = self.build_and_reg(client)
        user_db: User = User.objects.get(username=user_factory.username)

        assert reg_response.data is not None, 'Wrong response'
        assert reg_response.status_code == 201, 'Wrong status code'
        assert user_db is not None, 'User not found'
        assert user_db.username == user_factory.username, 'Wrong username expected'

    @pytest.mark.django_db
    def test_registrate_user_400(self, client: Any) -> None:
        """
        User registration test with 400 response because of wrong password repeat field

        Params:
            - client: A Django test client instance.

        Checks:
            - Response status code is 400
            - Response data is not None
            - Response data == expected data
            - User is not exists in database

        Returns:
            None

        Raises:
            AssertionError
        """
        user_factory: Any = UserFactory.build()
        post_response: Any = client.post(
            '/api/users/reg/',
            {
                'username': user_factory.username,
                'password': user_factory.password,
                'password_repeat': '123Qwert!@#'
            }
        )

        expected_response: dict[str, list[ErrorDetail]] = {
            'non_field_errors':
                [ErrorDetail(string='Password mismatch', code='invalid')]
        }

        assert post_response.data is not None, 'Wrong response'
        assert post_response.status_code == 400, 'Wrong status code'
        assert post_response.data == expected_response
        assert User.objects.filter(username=user_factory.username).exists() is False, 'User found'

    @pytest.mark.django_db
    def test_login_user(self, client: Any) -> None:
        """
        User authentication success test

        Params:
            - client: A Django test client instance.

        Checks:
            - Response status code is 400
            - Response data is not None
            - Response data == expected data

        Returns:
            None

        Raises:
            AssertionError
        """
        user_factory, reg_response = self.build_and_reg(client)

        response_auth: Any = self.user_login(client, data={
            'username': user_factory.username,
            'password': user_factory.password,
        })

        assert response_auth.status_code == 200, 'Wrong status code'
        assert response_auth.data is not None, 'Wrong response'
        assert response_auth.data['access'] is not None, 'No auth token'

    @pytest.mark.django_db
    def test_login_user_401(self, client: Any) -> None:
        """
        User login test with 403 response because of wrong password field

        Params:
            - client: A Django test client instance.

        Checks:
            - Response auth try 1 status code is 401
            - Response auth try 1 data is not None
            - Response auth try 1 data == expected data
            - Response auth try 2 status code is 401
            - Response auth try 2 data is not None
            - Response auth try 2 data == expected data

        Returns:
            None

        Raises:
            AssertionError
        """
        user_factory, reg_response = self.build_and_reg(client)
        response_auth_1: Any = self.user_login(client, data={
            'username': user_factory.username,
            'password': '123Qwert!@#',
        })
        response_auth_2: Any = self.user_login(client, data={
            'username': 'random_username',
            'password': user_factory.password
        })
        expected_response: dict[str, ErrorDetail] = {
            'detail': ErrorDetail(string='No active account found with the given credentials', code='no_active_account')
        }

        assert response_auth_1.status_code == 401, 'Wrong status code'
        assert response_auth_1.data is not None, 'Wrong response'
        assert response_auth_1.data == expected_response, 'Wrong data expected'
        assert response_auth_2.status_code == 401, 'Wrong status code'
        assert response_auth_2.data is not None, 'Wrong response'
        assert response_auth_2.data == expected_response, 'Wrong data expected'

    @staticmethod
    @pytest.mark.django_db
    def build_and_reg(client) -> tuple[Any, Any]:
        """
        Simple function to build user by user factory and add him to database

        Params:
            - client: A Django test client instance.

        Returns:
            Tuple with user entity and registration response
        """
        user_factory = UserFactory.build()
        reg_response = client.post(
            '/api/users/reg/',
            {
                'username': user_factory.username,
                'password': user_factory.password,
                'password_repeat': user_factory.password
            }
        )
        return user_factory, reg_response

    @staticmethod
    @pytest.mark.django_db
    def user_login(client: Any, data) -> Any:
        """
        Simple function that authenticate user by post request with user's data

        Params:
            - client: A Django test client instance.
            - data: dict with username and password params

        Returns:
            Tuple with user entity and registration response
        """
        response_auth: Any = client.post(
            '/api/users/auth/',
            {
                'username': data.get('username'),
                'password': data.get('password'),
            },
            format='json'
        )
        return response_auth
