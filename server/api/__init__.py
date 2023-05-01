def build_api_blueprint():
    from server.api.staff import build_staff_blueprint
    from server.core.engine import APIRoute

    return APIRoute.group(
        build_staff_blueprint(),
        url_prefix='/api',
        version=1,
        version_prefix='/v'
    )
