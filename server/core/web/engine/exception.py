from sanic import SanicException


class BadRequest(SanicException):
    status_code = 400
