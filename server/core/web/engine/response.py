from sanic import HTTPResponse, json

__all__ = ['APIResponse']


class APIResponse(HTTPResponse):

    @staticmethod
    def json(*args, **kwargs):
        return json(*args, **kwargs)
