from typing import Any

import pytest
from rest_framework.utils.serializer_helpers import ReturnDict

from posts.serializers import PostBaseSerializer
from tests.factories import PostFactory
from users.models import User


# ----------------------------------------------------------------
# post tests
class TestPost:
    @pytest.mark.django_db
    def test_create_post(self, client: Any, user_auth: dict[str, Any]) -> None:
        """
        Post create test

        Params:
            - client: A Django test client instance.
            - user_auth: A fixture that create user instance and login

        Checks:
            - Response status code is 201
            - Response data is not None
            - title field from response == title field from expected_response
            - id field from response == id field from expected_response
            - is_deleted field from response == is_deleted field from expected_response

        Returns:
            None

        Raises:
            AssertionError
        """
        expected_response: dict[str, str | int] = {
            'id': 1,
            'title': 'testPost',
            'body': 'testBody'
        }
        post_response: Any = client.post(
            '/api/posts/create/',
            data={'title': 'testPost', 'body': 'testBody'},
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer ' + user_auth.get('token')
        )

        assert post_response.status_code == 201, 'Post was not created successfully'
        assert post_response.data is not None, 'HttpResponseError'
        assert post_response.data.get('title') == expected_response.get('title'), 'Wrong title data'
        assert post_response.data.get('id') == expected_response.get('id'), 'Wrong id'
        assert post_response.data.get('body') == expected_response.get('body'), 'Wrong body data'

    @pytest.mark.django_db
    def test_create_post_403(self, client: Any, user_not_auth: User) -> None:
        """
        Post create test without authorization

        Params:
            - client: A Django test client instance.
            - user_not_auth: A fixture that create user instance but don't log in

        Checks:
            - Response status code is 403
            - Response data is not None
            - response data == data from expected response

        Returns:
            None

        Raises:
            AssertionError
        """
        expected_response: dict[str, str] = {
            'detail': 'Authentication credentials were not provided.'
        }

        post_response: Any = client.post(
            '/api/posts/create/',
            data={'title': 'testPost', 'body': 'testBody'},
            content_type='application/json',

        )

        assert post_response.status_code == 401, 'Status code error'
        assert post_response.data is not None, 'HttpResponseError'
        assert post_response.data == expected_response

    @pytest.mark.django_db
    def test_post_list(self, client: Any, user_auth: dict[str, Any]) -> None:
        """
        Post list test

        Params:
            - client: A Django test client instance.
            - user_auth: A fixture that create user instance and login

        Checks:
            - Response status code is 200
            - Response data is not None
            - response data == data from expected response

        Returns:
            None

        Raises:
            AssertionError
        """
        posts: Any = PostFactory.create_batch(2, user=user_auth.get('user'))
        expected_response: list[ReturnDict] = [
            PostBaseSerializer(posts[0]).data,
            PostBaseSerializer(posts[1]).data,
        ]
        response = client.get(
            '/api/posts/list/',
            HTTP_AUTHORIZATION='Bearer ' + user_auth.get('token')
        )

        assert response.status_code == 200, 'Status code error'
        assert response.data is not None, 'HttpResponseError'
        assert response.data == expected_response, 'Wrong data expected'

    @pytest.mark.django_db
    def test_post_list_401(self, client: Any, user_not_auth: User) -> None:
        """
        Post list test without authorization

        Params:
            - client: A Django test client instance.
            - user_not_auth: A fixture that create user instance but don't log in

        Checks:
            - Response status code is 401
            - Response data is not None
            - response data == data from expected response

        Returns:
            None

        Raises:
            AssertionError
        """
        PostFactory.create_batch(2, user=user_not_auth)
        expected_response: dict[str, str] = {"detail": 'Authentication credentials were not provided.'}
        response: Any = client.get('/api/posts/list/')

        assert response.status_code == 401, 'Status code error'
        assert response.data is not None, 'HttpResponseError'
        assert response.data == expected_response, 'Wrong data expected'

    @pytest.mark.django_db
    def test_delete_post(self, client: Any, user_auth: dict[str, Any]) -> None:
        """
        Board delete test

        Params:
            - client: A Django test client instance.
            - user_auth: A fixture that create user instance and login

        Checks:
            - Response status code is 204
            - Response data is None

        Returns:
            None

        Raises:
            AssertionError
        """
        post = PostFactory.create(user=user_auth.get('user'))
        delete_response: Any = client.delete(
            f'/api/posts/{post.id}/',
            HTTP_AUTHORIZATION='Bearer ' + user_auth.get('token')
        )

        assert delete_response.status_code == 204, 'Post was not deleted successfully'
        assert delete_response.data is None, 'HttpResponseError'

    @pytest.mark.django_db
    def test_delete_post_401(self, client: Any, user_auth: dict[str, Any]) -> None:
        """
        Post delete test

        Params:
            - client: A Django test client instance.
            - user_auth: A fixture that create user instance and login

        Checks:
            - Response status code is 401
            - Response data is not None
            - response data == data from expected response

        Returns:
            None

        Raises:
            AssertionError
        """
        post = PostFactory.create(user=user_auth.get('user'))
        expected_response: dict[str, str] = {
            'detail': 'Authentication credentials were not provided.'
        }
        delete_response: Any = client.delete(
            f'/api/posts/{post.id}/',
        )

        assert delete_response.status_code == 401, 'Board was deleted successfully'
        assert delete_response.data is not None, 'HttpResponseError'
        assert delete_response.data == expected_response, 'Wrong data'