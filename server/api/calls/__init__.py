def build_calls_blueprint():
    from api.calls.list import CallsAPIView
    from core.web.engine.route import APIRoute

    route = APIRoute('calls', url_prefix='/calls')

    route.add(CallsAPIView.as_view(), '/')

    return route
