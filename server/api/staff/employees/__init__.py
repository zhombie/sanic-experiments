def build_staff_employees_blueprint():
    from api.staff.employees.list import EmployeesAPIView
    from core.web.engine.route import APIRoute

    route = APIRoute('staff-employees', url_prefix='/employees')

    route.add(EmployeesAPIView.as_view(), '/')

    return route
