"""Main API definition."""
import endpoints
from settings import WEB_CLIENT_ID
from settings import FIREBASE_GOOGLE_AUTH_CLIENT_ID

ALLOWED_CLIENT_IDS = [endpoints.API_EXPLORER_CLIENT_ID,
                      WEB_CLIENT_ID,
                      FIREBASE_GOOGLE_AUTH_CLIENT_ID]

api_definition = endpoints.api(name='scaffold', version='v1',
                               description='Scaffold API',
                               allowed_client_ids=ALLOWED_CLIENT_IDS,
                               auth_level=endpoints.AUTH_LEVEL.REQUIRED)
