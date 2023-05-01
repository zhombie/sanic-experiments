from server.api.serialization import on_api_request
from server.core.web.engine.view import APIView


class BaseAPIView(APIView):
    decorators = [on_api_request]
