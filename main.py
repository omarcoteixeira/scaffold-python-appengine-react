"""Main module that starts API server."""
import endpoints

from api import UserProfileAPI

API = endpoints.api_server([UserProfileAPI])
