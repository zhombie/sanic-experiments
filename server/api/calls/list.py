from api.base import BaseAPIView
from di.di import di


class CallsAPIView(BaseAPIView):

    async def get(self, _):
        calls = await di.calls_repository.get_calls()
        return calls
