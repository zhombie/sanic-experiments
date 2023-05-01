from sanic import Blueprint
from sanic.blueprint_group import BlueprintGroup

__all__ = ['APIRoute', 'APIRouteGroup']


class APIRoute(Blueprint):

    def add(self, *args, **kwargs):
        return self.add_route(*args, **kwargs)


class APIRouteGroup(BlueprintGroup):
    pass
