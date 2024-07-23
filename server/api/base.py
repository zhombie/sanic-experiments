from api.serialization import on_api_request
from core.web.engine.view import APIView


class BaseAPIView(APIView):
    decorators = [on_api_request]
