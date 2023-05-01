def build_staff_blueprint():
    from server.api.staff.employees import build_staff_employees_blueprint
    from core.engine import APIRoute

    return APIRoute.group(
        build_staff_employees_blueprint(),
        url_prefix='/staff'
    )
