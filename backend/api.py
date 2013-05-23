from backend.greetings import services
from google.appengine.ext import endpoints


AVAILABLE_SERVICES = [
    services.GreetingService,
]

app = endpoints.api_server(AVAILABLE_SERVICES, restricted=False)