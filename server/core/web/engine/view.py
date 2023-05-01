from sanic import empty
from sanic.views import HTTPMethodView

__all__ = ['APIView']


class APIView(HTTPMethodView):

    # noinspection PyUnusedLocal
    @classmethod
    async def options(cls, _, *args, **kwargs):
        return empty()
