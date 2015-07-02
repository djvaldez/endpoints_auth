import endpoints
import logging

from functools import wraps
from webapp2_extras.appengine.auth.models import User


MESSAGE_UNAUTHORIZED = "You're not authorized to perform this action."


def auth_required():
    """ Wrapper for validating an endpoints method """

    def decorator(endpoints_method):
        @wraps(endpoints_method)
        def validate(*args, **kwargs):
            """ Validates the User ID and token sent in an endpoints request."""

            # Get the headers from the self arg
            headers = args[0].request_state.headers
            token = headers.get('Token')
            if headers.get('User-Id') is None:
                raise endpoints.UnauthorizedException(MESSAGE_UNAUTHORIZED)

            user_id = int(headers.get('User-Id'))
            user, timestamp = User.get_by_auth_token(user_id, token)
            if user:
                return endpoints_method(*args, **kwargs)
            else:
                logging.warn('Invalid API request! User ID:%s, token:%s'
                             %(user_id, token))
                raise endpoints.UnauthorizedException(MESSAGE_UNAUTHORIZED)
        return validate
    return decorator
