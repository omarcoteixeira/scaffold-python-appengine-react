"""Decorators for namespace management."""
import endpoints
import pdb


def authorize(func):
    """Validate if is logged.

    Raises:
        UnauthorizedException: If user is not authenticated.

    """
    def func_wrapper(*args, **kwargs):
        """Wrap the function."""
        user = endpoints.get_current_user()
        if not user:
            raise endpoints.UnauthorizedException("Authorization required.")
        return func(*args, **kwargs)
    return func_wrapper
