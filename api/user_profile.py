"""User Profile API."""
import endpoints

from google.appengine.ext import ndb
from protorpc import message_types
from protorpc import remote

from api import api_definition
from entities import messages
from entities import models
from utils.decorators import authorize


@api_definition.api_class(resource_name='profile', path='profile')
class UserProfileAPI(remote.Service):
    """Crud operations for User Profile."""

    @endpoints.method(message_types.VoidMessage,
                      messages.UserProfileAddResponseMessage,
                      path='me', http_method='GET',
                      name='me')
    @authorize
    def me(self, request):
        """Simple GET to check if Google Endpoint inject the User.

        Returns:
            Returns the Authenticated User

        """
        user_email = endpoints.get_current_user().email()
        result = messages.UserProfileAddResponseMessage(email=user_email)
        return result

    @endpoints.method(messages.UserProfileAddRequestMessage,
                      messages.UserProfileAddRequestMessage,
                      path='add', http_method='POST',
                      name='add')
    @authorize
    def add(self, request):
        """POST to insert a new user in database.

        Returns:
            Returns the created user

        """
        email = request.email
        profile_key = ndb.Key(models.UserProfile, email)

        profile = profile_key.get()
        if not profile:
            profile = models.UserProfile(id=email, email=email)
            profile.put()

        return request
