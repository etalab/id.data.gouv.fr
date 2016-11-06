import datetime
from django.utils import timezone

from oauth2_provider.tests.test_authorization_code import BaseTest
from oauth2_provider.models import AccessToken


class ProfileTest(BaseTest):

    def createToken(self, **kwargs):
        defaults = {
            'user': self.test_user, 'token': '1234567890', 'scope': 'read',
            'application': self.application,
            'expires': timezone.now() + datetime.timedelta(days=1),
        }
        defaults.update(kwargs)
        return AccessToken.objects.create(**defaults)

    def test_profile_access_requires_auth(self):
        response = self.client.get('/api/profile/')
        self.assertEquals(response.status_code, 302)

    def test_profile_data(self):
        token = self.createToken()
        response = self.client.get(
            '/api/profile/', HTTP_AUTHORIZATION='Bearer {}'.format(token))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['id'], self.test_user.id)
        self.assertNotIn('email', response.json())

    def test_access_with_wrong_token(self):
        self.createToken()
        response = self.client.get(
            '/api/profile/', HTTP_AUTHORIZATION='Bearer 123')
        self.assertEquals(response.status_code, 401)
        self.assertIn('WWW-Authenticate', response)

    def test_access_with_scope(self):
        token = self.createToken(scope='email')
        self.assertEquals(token.scope, 'email')
        response = self.client.get('/api/profile/',
            HTTP_AUTHORIZATION='Bearer {}'.format(token)
        )
        self.assertEquals(response.json()['email'], self.test_user.email)
