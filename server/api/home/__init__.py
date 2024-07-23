def build_home_blueprint():
    from api.home.index import HomeAPIView
    from core.web.engine.route import APIRoute

    route = APIRoute('home', url_prefix='/')

    route.add(HomeAPIView.as_view(), '/')

    return route
