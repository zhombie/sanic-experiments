from sanic import Blueprint, HTTPResponse, Sanic, json
from sanic.blueprint_group import BlueprintGroup
from sanic.views import HTTPMethodView
from sanic_ext import CountedRequest


class App(Sanic):
    pass


class APIView(HTTPMethodView):
    pass


class APIRoute(Blueprint):

    def add(self, *args, **kwargs):
        return self.add_route(*args, **kwargs)


class APIRouteGroup(BlueprintGroup):
    pass


class APIRequest(CountedRequest):

    def to_dict(self):
        return {
            'id': str(self.id),
            'method': self.method,
            'url': self.url,
            'headers': {k: v for k, v in self.headers.items()},
            'count': self.count
        }


class APIResponse(HTTPResponse):

    @staticmethod
    def json(*args, **kwargs):
        return json(*args, **kwargs)
