from google.appengine.ext import endpoints


def login_required():
    current_user = endpoints.get_current_user()
    if current_user is None:
        raise endpoints.UnauthorizedException('Invalid token.')
    return current_user
