import enum


@enum.unique
class HTTPMethod(enum.Enum):
    GET = 'GET'
    POST = 'POST'

    @staticmethod
    def of(value) -> 'HTTPMethod':
        return HTTPMethod(value)

    def is_get(self):
        return self == HTTPMethod.GET

    def is_post(self):
        return self == HTTPMethod.POST
