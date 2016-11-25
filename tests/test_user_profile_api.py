"""Unit tests for User profile API."""
import unittest
import mock
import logging
import endpoints

from protorpc import message_types
from api import UserProfileAPI
from entities import messages
from google.appengine.ext import testbed
from entities import models


class UserProfileApiTest(unittest.TestCase):
    """Tests for User Profile Api."""

    def setUp(self):
        """Setup API settings for tests."""
        logging.getLogger().setLevel(logging.INFO)
        self.api = UserProfileAPI()
        self.void_resource = message_types.VoidMessage()
        self.email_test = 'me@test.com'

        tb = testbed.Testbed()
        tb.setup_env(current_version_id='testbed.version')
        tb.activate()
        tb.init_all_stubs()
        self.testbed = tb

        profile = models.UserProfile(id=self.email_test, email=self.email_test)
        profile.put()

    def tearDown(self):
        """Destroy settings created for tests."""
        self.testbed.deactivate()

    @mock.patch('api.user_profile.endpoints.get_current_user')
    def test_success_get_me(self, user_mock):
        """Basic scenary test: get me."""
        user_mock.return_value.email.return_value = self.email_test
        response = self.api.me(self.void_resource)
        self.assertEquals(response.email, self.email_test)

    @mock.patch('api.user_profile.endpoints.get_current_user')
    def test_success_add_profile(self, user_mock):
        """Basic scenary test: Add user."""
        user_mock.return_value.email.return_value = self.email_test
        new_user_mail = 'new@test.com.br'
        request = messages.UserProfileAddRequestMessage(email=new_user_mail)
        response = self.api.add(request)
        self.assertEquals(response.email, new_user_mail)

    @mock.patch('api.user_profile.endpoints.get_current_user')
    def test_not_authorized_add_profile(self, user_mock):
        """Basic scenary test: Not authorized scenary test: Add user."""
        user_mock.return_value.email.return_value = self.email_test
        new_user_mail = 'new@test.com.br'
        request = messages.UserProfileAddRequestMessage(email=new_user_mail)
        response = self.api.add(request)
        self.assertEquals(response.email, new_user_mail)
        self.assertNotEquals(response.email, self.email_test)

if __name__ == '__main__':
    unittest.main()
