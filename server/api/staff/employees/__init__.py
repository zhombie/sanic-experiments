def build_staff_employees_blueprint():
    from server.api.staff.employees.list import EmployeesAPIView
    from server.core.engine import APIRoute

    route = APIRoute('staff-employees', url_prefix='/employees')

    route.add(EmployeesAPIView.as_view(), '/')

    return route
