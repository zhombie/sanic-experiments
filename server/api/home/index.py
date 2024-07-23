from api.base import BaseAPIView


class HomeAPIView(BaseAPIView):

    async def get(self, _):
        return 'Hello, World!'
