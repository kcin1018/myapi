import pytest
from rest_framework.test import APITestCase
from rest_framework.utils.serializer_helpers import ReturnDict
from django.contrib.auth.models import User
#from .models import *
from api.tests import factories

pytestmark = pytest.mark.django_db(transaction=True)


class UsersTest(APITestCase):
    def seed(self):
        # create user for authentication
        self.user = factories.UserFactory()

        for i in range(0, 14):
            user = factories.UserFactory()

        # store the id for testing
        self.userId = user.id

    def test_users_index(self):
        # seed the database
        self.seed()

        # make the request
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/users/')

        # test the results
        assert response.status_code == 200
        assert isinstance(response.data, dict);
        assert len(response.data.get('results')) == 15

    def test_users_show(self):
        # seed the database
        self.seed()

        # make the request
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/users/' + str(self.userId) + '/')

        # test the results
        assert response.status_code == 200
        assert isinstance(response.data, ReturnDict)
        assert response.data.get('id') == self.userId

