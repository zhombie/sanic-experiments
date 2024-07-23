def build_staff_blueprint():
    from api.staff.employees import build_staff_employees_blueprint
    from core.web.engine.route import APIRoute

    return APIRoute.group(
        build_staff_employees_blueprint(),
        url_prefix='/staff'
    )
