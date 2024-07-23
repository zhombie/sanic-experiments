from api.base import BaseAPIView


class HomeAPIView(BaseAPIView):

    @classmethod
    async def get(cls, _):
        return 'Hello, World!'
