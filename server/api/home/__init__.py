def build_home_blueprint():
    from server.api.home.index import HomeAPIView
    from core.engine import APIRoute

    route = APIRoute('home', url_prefix='/')

    route.add(HomeAPIView.as_view(), '/')

    return route
