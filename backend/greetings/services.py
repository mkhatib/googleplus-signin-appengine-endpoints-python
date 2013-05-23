from backend.greetings import messages as greetings_messages
from backend.users import users

from google.appengine.ext import endpoints
from protorpc import message_types
from protorpc import remote

import os

ALLOWED_CLIENT_IDS = [
    os.environ['GOOGLE_CLIENT_ID'],
    endpoints.API_EXPLORER_CLIENT_ID,
]


@endpoints.api(name='greetings', version='v1', description='Greetings API',
               allowed_client_ids=ALLOWED_CLIENT_IDS)
class GreetingService(remote.Service):

    @endpoints.method(message_types.VoidMessage, greetings_messages.Greeting,
                      name='get', path='greetings', http_method='GET')
    def get_greeting(self, request):
        # This requires a valid OAuth token and is passed using the gapi.auth
        # setup in main.js file.
        user = users.login_required()
        return greetings_messages.Greeting(
            msg='Hello {} from backend!'.format(user))
