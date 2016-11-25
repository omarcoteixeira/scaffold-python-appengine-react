"""Models module."""
from google.appengine.ext import ndb


class UserProfile(ndb.Model):
    """User Profile class model."""

    email = ndb.StringProperty()
    imageUrl = ndb.StringProperty(indexed=False)
