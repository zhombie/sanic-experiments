def build_api_blueprint():
    from api.home import build_home_blueprint
    from api.staff import build_staff_blueprint
    from core.web.engine.route import APIRoute

    return APIRoute.group(
        build_home_blueprint(),
        build_staff_blueprint(),
        url_prefix='/api',
        version=1,
        version_prefix='/v'
    )
