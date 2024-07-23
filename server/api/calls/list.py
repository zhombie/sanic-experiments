from api.base import BaseAPIView
from di.di import di


class CallsAPIView(BaseAPIView):

    @classmethod
    async def get(cls, _) -> dict:
        calls = await di.calls_repository.get_calls()
        count = await di.calls_repository.get_calls_count()
        return {
            'calls': calls,
            'count': count
        }
