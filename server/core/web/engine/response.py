from sanic import HTTPResponse, json

__all__ = ['APIResponse']


class APIResponse(HTTPResponse):

    @staticmethod
    def json(*args, **kwargs):
        print(f'APIResponse#json() -> args: {args}, kwargs: {kwargs}')
        return json(*args, **kwargs)
