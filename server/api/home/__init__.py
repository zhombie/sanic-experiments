def build_home_blueprint():
    from server.api.home.index import HomeAPIView
    from server.core.web.engine.route import APIRoute

    route = APIRoute('home', url_prefix='/')

    route.add(HomeAPIView.as_view(), '/')

    return route
