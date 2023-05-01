from server.api.serialization import on_api_request
from server.core.engine import APIView


class BaseAPIView(APIView):
    decorators = [on_api_request]
