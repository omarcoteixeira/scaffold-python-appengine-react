"""RPC Messages module."""
from protorpc import messages as m


class UserProfileMessage(m.Message):
    """Message for a User Profile."""

    email = m.StringField(1)
    imageUrl = m.StringField(2)


class UserOAuthProvider(m.Enum):
    """User OAuth Provider (Firebase) for UserOAuthProvider."""

    GooglePlus = 1
    Facebook = 2
    Twitter = 3


class UserProfileAddRequestMessage(m.Message):
    """Message for a add new User Profile."""

    email = m.StringField(1)
    oauthProvider = m.StringField(2, required=False)
    imageUrl = m.StringField(3, required=False)


class UserProfileAddResponseMessage(m.Message):
    """Response message for add a new User."""

    email = m.StringField(1)
    imageUrl = m.StringField(3, required=False)
